import datetime
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

checkprogram = uic.loadUiType("check.ui")[0]

class WindowClass(QMainWindow, checkprogram) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('비콘찍으라')
        self.stackedWidget.setCurrentIndex(1)
        self.db = pymysql.connect(host ='localhost', port = 3306,
                                  user ='root', password = '0000', db = 'check',charset = 'utf8')
        self.cursor = self.db.cursor()
        self.pw_check.setEchoMode(QLineEdit.Password)
        self.main_button.clicked.connect(self.mainpage)
        self.main_button_2.clicked.connect(self.mainpage)
        self.login_button.clicked.connect(self.mainpage)
        self.logout_button.clicked.connect(self.start)
        self.review_button.clicked.connect(self.review)
        self.main2_button.clicked.connect(self.mainpage)
        self.manager_button.clicked.connect(self.manager_view)
        self.attendance_button.clicked.connect(self.check)
        # self.schedule_button.clicked.connect(self.schedule_view_teacher)
        self.message_button.clicked.connect(self.message_Confirm)
        self.bcon_button.clicked.connect(self.entrance_f)
        self.bcon_button_2.clicked.connect(self.leave_f)
        self.outing_button.clicked.connect(self.outing_f)
        self.comeback_button.clicked.connect(self.comeback_f)
        self.manager_end_button.clicked.connect(self.start)
        self.manager_end_button_2.clicked.connect(self.start)
        self.manager_end_button_3.clicked.connect(self.start)
        self.schedule_check_button.clicked.connect(self.schedule_view_student)
        self.calendarWidget.selectionChanged.connect(self.schedule_f)
        self.schedule_add_button.clicked.connect(self.calendarlist_add)
        self.schedule_del_button.clicked.connect(self.calendarlist_del)
        self.schedule_Lookup_button.clicked.connect(self.calendarlist_lookup)
        self.schedule_button.clicked.connect(self.calendarlist_teacher)
        self.date_list.cellClicked.connect(self.cellclicked_event)
        self.date_list.cellDoubleClicked.connect(self.cellclicked_event)
        self.tableWidget.cellClicked.connect(self.class_clicked)
        self.tableWidget.cellDoubleClicked.connect(self.class_clicked)

        self.message_st_button.clicked.connect(self.message_view_student)
        self.message_send_button.clicked.connect(self.message_send)
        self.lookup_message.clicked.connect(self.message_view)
        self.message_button.clicked.connect(self.message_view_teacher)
        self.find_button.clicked.connect(self.find_course_review)
        self.classview_button.clicked.connect(self.change_class_review)
        self.review_add_button.clicked.connect(self.review_add)
        self.Professor_date_add.clicked.connect(self.Professor_add)
        self.calendarWidget_2.clicked.connect(self.calendarlist_teacher)



# 화면전환용 ----------------------------------------------

    def mainpage(self):
        self.stackedWidget.setCurrentIndex(0)
        # self.selftest()
        self.login_page()

    def start(self):
        self.stackedWidget.setCurrentIndex(1)
        self.logout_check()

    # def signup_add(self):
    #     self.stackedWidget.setCurrentIndex(2)

    def message_view_student(self):
        self.stackedWidget.setCurrentIndex(3)

    def review(self):
        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_5.setCurrentIndex(0)


    def schedule_view_student(self):
        self.stackedWidget.setCurrentIndex(5)
        self.show_calendar()

    def manager_view(self):
        self.stackedWidget.setCurrentIndex(6)


    def schedule_view_teacher(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def message_Confirm(self):
        self.stackedWidget_2.setCurrentIndex(2)


# 관리자모드 -------------------------------------------------

    # def signup(self):
    #
    #     self.cursor.execute(f"INSERT INTO login_data VALUES('{self.name_line.text()}''{self.pw_line.text}''{self.pw2_line.text}')")
    #     self.cursor.execute("SELECT * FROM check.check_list")
    #     result = self.cursor.fetchall()
    #     print(result)
    #     self.db.close()

    def check(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.cursor.execute("update check_list set 출석여부 = '결석' where (입실시간 is null) and (퇴실시간 is null)")
        self.cursor.execute("update check_list set 출석여부 = '지각' where timediff(입실시간,'09:20')>0")
        self.cursor.execute("update check_list set 출석여부 = '조퇴' where timediff(퇴실시간,'17:00')>0")
        self.cursor.execute("SELECT 이름,입실시간,퇴실시간,출석여부 from check_list")
        result = self.cursor.fetchall()
        self.check_widget.setRowCount(len(result))
        self.check_widget.setColumnCount(len(result[0]))
        self.check_widget.setHorizontalHeaderLabels(['이름', '입실시간', '퇴실시간','출석여부'])
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.check_widget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.check_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def calendarlist_teacher(self):
        try:
            self.stackedWidget_2.setCurrentIndex(1)
            self.cursor.execute("SELECT distinct * FROM check.message_date")
            result = self.cursor.fetchall()
            self.date_widget.setRowCount(len(result))
            self.date_widget.setColumnCount(len(result[0]))
            self.date_widget.setHorizontalHeaderLabels(['날짜', '이름', '일정'])
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.date_widget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
            self.date_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

            now = self.calendarWidget_2.selectedDate()
            self.data_lineEdit.setText(f"{now.toString(Qt.DefaultLocaleLongDate)}")
            print(now)

        except:
            QtWidgets.QMessageBox.about(self, " ","등록된 일정이 없습니다")


    def message_view_teacher(self):
        try:
            self.cursor.execute("SELECT distinct * FROM check.message")
            result = self.cursor.fetchall()
            self.message_widget.setRowCount(len(result))
            self.message_widget.setColumnCount(len(result[0]))
            self.message_widget.setHorizontalHeaderLabels(['이름', '메세지'])
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.message_widget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
            self.message_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        except:
            QtWidgets.QMessageBox.about(self, " ", "메세지가 없습니다")

    def Professor_add(self):
        now = self.calendarWidget_2.selectedDate()
        self.data_lineEdit.setText(f"{now.toString(Qt.DefaultLocaleLongDate)}")
        self.data_lineEdit.clear()
        print(self.data_lineEdit.text())
        a = ['이상복','류홍걸','조동현']
        show = self.Professor_name.currentText()
        for i in range(len(a)):
            if show == a[i]:
                self.cursor.execute(f"insert into check.message_date (날짜,이름,메세지) values ('{now.toString(Qt.DefaultLocaleLongDate)}','{show}','{self.Professor_date.text()}')")
                self.db.commit()
                self.Professor_date.clear()
                self.stackedWidget_2.setCurrentIndex(1)
                self.cursor.execute("SELECT distinct * FROM check.message_date")
                result = self.cursor.fetchall()
                self.date_widget.setRowCount(len(result))
                self.date_widget.setColumnCount(len(result[0]))
                self.date_widget.setHorizontalHeaderLabels(['날짜', '이름', '일정'])
                for i in range(len(result)):
                    for j in range(len(result[i])):
                        self.date_widget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
                self.date_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

                now = self.calendarWidget_2.selectedDate()
                self.data_lineEdit.setText(f"{now.toString(Qt.DefaultLocaleLongDate)}")
                print(now)
            else:
                continue

# 메인페이지 -----------------------------------------------

    def login_page(self):
        try:
            self.cursor.execute(
                f"SELECT * from check_list where 아이디 = '{self.id_check.text()}' and 비밀번호 = '{self.pw_check.text()}'")
            self.login = self.cursor.fetchone()
            if not bool(self.login):
                self.stackedWidget.setCurrentIndex(1)
            else:
                print('로그인성공')
                # QtWidgets.QMessageBox.about(self, "로그인성공", f"{self.login[1]}님 반갑습니다!")
            self.name_line.setText(f"{self.login[1]}")
        except:
            QtWidgets.QMessageBox.about(self, " ", "로그인정보가 없습니다.")

    def logout_check(self):
        self.id_check.clear()
        self.pw_check.clear()
        self.name_line.clear()
        self.entrance_line.clear()
        self.leave_line.clear()
        self.outing_line.clear()
        self.comeback_line.clear()
        self.date_list.clear()
        self.date_detail.clear()
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)


    def entrance_f(self):
        self.stackedWidget_3.setCurrentIndex(1)
        check = QMessageBox.question(self, '','입실 하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if check == QMessageBox.Yes:
            QMessageBox.information(self, '','입실하였습니다')

            now = datetime.datetime.now()
            time = now.strftime("%X")
            self.entrance_line.setText(f'{time}')
            self.cursor.execute(f"update check_list set 입실시간 = '{time}' where 이름 = '{self.login[1]}'")
            self.db.commit()
            print(time)

    def leave_f(self):
        check = QMessageBox.question(self, '','퇴실 하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if check == QMessageBox.Yes:
            QMessageBox.information(self, '','퇴실하였습니다')
        now = datetime.datetime.now()
        time = now.strftime("%X")
        self.leave_line.setText(f'{time}')
        self.cursor.execute(f"update check_list set 퇴실시간 = '{time}' where 이름 = '{self.login[1]}'")
        self.db.commit()
        print(time)

    def outing_f(self):
        self.stackedWidget_4.setCurrentIndex(1)
        check = QMessageBox.question(self, ' ','외출 하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if check == QMessageBox.Yes:
            QMessageBox.information(self, ' ','외출하였습니다')
        now = datetime.datetime.now()
        time = now.strftime("%X")
        self.outing_line.setText(f'{time}')
        print(time)

    def comeback_f(self):
        check = QMessageBox.question(self, ' ','복귀 하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if check == QMessageBox.Yes:
            QMessageBox.information(self, ' ','복귀하였습니다')
        now = datetime.datetime.now()
        time = now.strftime("%X")
        self.comeback_line.setText(f'{time}')
        print(time)

    def schedule_f(self):
        now = self.calendarWidget.selectedDate()
        self.date_line.setText(f"{now.toString(Qt.DefaultLocaleLongDate)}")
        # print(f"{now},{self.login[1]}")
        calendar = self.date_detail.text()
        print(calendar)

    def cellclicked_event(self,row,col):
        self.data = self.date_list.item(row,col)
        self.cellchoice = self.data.text()
        print(self.cellchoice)

    def class_clicked(self,row,col):
        self.data = self.tableWidget.item(row, col)
        self.cellchoice = self.data.text()
        print(self.cellchoice)


    def calendarlist_add(self):

        now = self.calendarWidget.selectedDate()
        self.date_line.setText(f"{now.toString(Qt.DefaultLocaleLongDate)}")
        self.cursor.execute(f"insert into check.message_date (날짜,이름,메세지) values ('{now.toString(Qt.DefaultLocaleLongDate)}','{self.login[1]}','{self.date_detail.text()}')")
        self.db.commit()

        self.cursor.execute(f"SELECT distinct * FROM check.message_date WHERE 이름 = '{self.login[1]}'")
        result = self.cursor.fetchall()
        self.date_list.setRowCount(len(result))
        self.date_list.setColumnCount(len(result[0]))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.date_list.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.date_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.date_detail.clear()

    def calendarlist_del(self):

        self.cursor.execute(f"delete from check.message_date where 메세지 = '{self.cellchoice}'")
        self.db.commit()

        self.cursor.execute(f"SELECT distinct * FROM check.message_date WHERE 이름 = '{self.login[1]}'")
        result = self.cursor.fetchall()
        self.date_list.setRowCount(len(result))
        self.date_list.setColumnCount(len(result))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.date_list.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.date_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def calendarlist_lookup(self):
        try:
            self.calendar_list_view =[]
            self.cursor.execute(f"SELECT distinct * FROM check.message_date WHERE 이름 = '{self.login[1]}'")
            result = self.cursor.fetchall()
            # print(result)
            self.date_list.setRowCount(len(result))
            self.date_list.setColumnCount(len(result[0]))
            self.date_list.setHorizontalHeaderLabels(['날짜', '이름','일정'])
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.date_list.setItem(i, j, QTableWidgetItem(str(result[i][j])))
            self.date_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

            self.cursor.execute(f"SELECT * FROM check.message_date WHERE 날짜")
            result = self.cursor.fetchall()
            # print(result[0][0])
            for i in range(len(result)):
                self.calendar_list_view.append(result[i][0])
            print(self.calendar_list_view)
        except:
            QtWidgets.QMessageBox.about(self, " ",'등록된 일정이 없습니다')

    def show_calendar(self):
        self.calendar_list_view = []
        self.cursor.execute(f"SELECT * FROM check.message_date WHERE 날짜")
        result = self.cursor.fetchall()
        # print(result[0][0])
        for i in range(len(result)):
            self.calendar_list_view.append(result[i][0])
        print(self.calendar_list_view)

        self.calendarWidget.setVerticalHeaderFormat(0)

        fm = QTextCharFormat()
        fm.setForeground(Qt.red)
        fm.setBackground(Qt.yellow)

        for dday in self.calendar_list_view:
            dday2 = QDate.fromString(dday,Qt.DefaultLocaleLongDate)
            self.calendarWidget.setDateTextFormat(dday2, fm)

    def message_send(self):
        self.cursor.execute(f"insert into check.message (이름,내용) values ('{self.login[1]}','{self.message_add_student.text()}')")
        self.db.commit()
        self.message_add_student.clear()

    def message_view(self):
        self.cursor.execute(f"SELECT distinct * FROM check.message WHERE 이름 = '{self.login[1]}'")
        result = self.cursor.fetchall()
        self.tableWidget_message.setRowCount(len(result))
        self.tableWidget_message.setColumnCount(len(result[0]))
        self.tableWidget_message.setHorizontalHeaderLabels(['이름', '메세지'])
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.tableWidget_message.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.tableWidget_message.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

# 수강평 -----------------------------------------------
    def find_course_review(self):
        show = self.comboBox.currentText()
        self.tableWidget.clear()

        if show == '전체보기':
            self.stackedWidget_5.setCurrentIndex(0)
            self.cursor.execute(f"SELECT distinct * FROM check.class_list")
            result = self.cursor.fetchall()
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(['훈련기관명', '훈련과정명', '훈련구분', '훈련기간'])
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        if show == '훈련 기관명':
            self.tableWidget.clear()

            try:
                self.cursor.execute(f"SELECT * FROM check.class_list WHERE 훈련기관명 LIKE '%{self.lineEdit_5.text()}%'")
                result = self.cursor.fetchall()
                self.tableWidget.setRowCount(len(result))
                self.tableWidget.setColumnCount(len(result[0]))
                self.tableWidget.setHorizontalHeaderLabels(['훈련기관명', '훈련과정명', '훈련구분', '훈련기간'])
                for i in range(len(result)):
                    for j in range(len(result[i])):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
                self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            except:
                self.stackedWidget_5.setCurrentIndex(0)
                QtWidgets.QMessageBox.about(self, " ","검색결과가 없습니다")

        if show == '훈련 과정명':
            self.tableWidget.clear()
            try:
                self.cursor.execute(f"SELECT * FROM check.class_list WHERE 훈련과정명 LIKE '%{self.lineEdit_5.text()}%'")
                result = self.cursor.fetchall()
                self.tableWidget.setRowCount(len(result))
                self.tableWidget.setColumnCount(len(result[0]))
                self.tableWidget.setHorizontalHeaderLabels(['훈련기관명', '훈련과정명', '훈련구분', '훈련기간'])
                for i in range(len(result)):
                    for j in range(len(result[i])):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
                self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            except:
                self.stackedWidget_5.setCurrentIndex(0)
                QtWidgets.QMessageBox.about(self, " ", "검색결과가 없습니다")

    def change_class_review(self):
        self.lineEdit.clear()
        self.stackedWidget_5.setCurrentIndex(2)

    def review_add(self):
        review = self.lineEdit.text()
        self.cursor.execute(f"insert into check.review_list (내용) values ('{self.lineEdit.text()}')")
        self.db.commit()
        self.listWidget.addItem(review)
        self.lineEdit.clear()

if __name__ == "__main__" :

    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

