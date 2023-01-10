import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *

checkprogram = uic.loadUiType("check.ui")[0]

class WindowClass(QMainWindow, checkprogram) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('비콘찍으라')
        self.stackedWidget.setCurrentIndex(1)
        self.db = pymysql.connect(host='localhost', port=3306,
                                  user='root', password='0000', db='check',charset='utf8')
        self.cursor = self.db.cursor()
        self.pw_check.setEchoMode(QLineEdit.Password)
        self.main_button.clicked.connect(self.mainpage)
        self.login_button.clicked.connect(self.mainpage)
        self.logout_button.clicked.connect(self.start)
        self.review_button.clicked.connect(self.review)
        self.main2_button.clicked.connect(self.mainpage)
        self.manager_button.clicked.connect(self.manager_view)
        self.attendance_button.clicked.connect(self.check)
        self.schedule_button.clicked.connect(self.schedule_view_teacher)
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
        self.schedule_update_button.clicked.connect(self.calendarlist_update)
        self.schedule_del_button.clicked.connect(self.calendarlist_del)
        self.schedule_Lookup_button.clicked.connect(self.calendarlist_lookup)
        self.schedule_button.clicked.connect(self.calendarlist_teacher)
        self.date_list.cellClicked.connect(self.cellclicked_event)


# 화면전환용 ----------------------------------------------

    def mainpage(self):
        self.stackedWidget.setCurrentIndex(0)
        self.login_page()

    def start(self):
        self.stackedWidget.setCurrentIndex(1)
        self.logout_check()

    def signup_add(self):
        self.stackedWidget.setCurrentIndex(2)

    def message_send(self):
        self.stackedWidget.setCurrentIndex(3)

    def review(self):
        self.stackedWidget.setCurrentIndex(4)

    def schedule_view_student(self):
        self.stackedWidget.setCurrentIndex(5)

    def manager_view(self):
        self.stackedWidget.setCurrentIndex(6)

    def schedule_view_teacher(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def message_Confirm(self):
        self.stackedWidget_2.setCurrentIndex(2)

# 관리자모드 -------------------------------------------------

    def signup(self):
        # pass
        self.cursor.execute(f"INSERT INTO login_data VALUES('{self.name_line.text()}''{self.pw_line.text}''{self.pw2_line.text}')")
        self.cursor.execute("SELECT * FROM check.check_list")
        result = self.cursor.fetchall()
        print(result)
        self.db.close()

    def check(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.cursor.execute("select * from check_list where 퇴실시간 is null")
        checklist = self.cursor.fetchall()
        # print(checklist)
        self.cursor.execute("SELECT 이름,입실시간,퇴실시간,출석여부 from check_list")
        result = self.cursor.fetchall()
        self.check_widget.setRowCount(len(result))
        self.check_widget.setColumnCount(len(result[0]))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.check_widget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.check_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def calendarlist_teacher(self):
        self.cursor.execute("SELECT * FROM check.message_date;")
        result = self.cursor.fetchall()
        self.date_widget.setRowCount(len(result))
        self.date_widget.setColumnCount(len(result[0]))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.date_widget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.date_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)





# 메인페이지 -----------------------------------------------

    def login_page(self):
        #
        # if self.id_check.text() == "":
        #     QtWidgets.QMessageBox.about(self, " ","아이디를 입력하세요")
        self.cursor.execute(f"SELECT * from check_list where 아이디 = '{self.id_check.text()}' and 비밀번호 = '{self.pw_check.text()}'")
        self.login = self.cursor.fetchone()
        print(self.login[1])
        QtWidgets.QMessageBox.about(self,"로그인성공",f"{self.login[1]}님 반갑습니다!")
        self.name_line.setText(f"{self.login[1]}")

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


    def entrance_f(self):
        watch = QTime.currentTime()
        time = watch.toString(Qt.DefaultLocaleLongDate)
        print(time)
        # self.cursor.execute("SELECT now()")
        # time = self.cursor.fetchall()[0][0]
        self.entrance_line.setText(f'{time}')
        self.cursor.execute(f"update check_list set 입실시간 = '{time}' where 이름 = '{self.login[1]}'")
        self.db.commit()
        print(time)

    def leave_f(self):
        watch = QTime.currentTime()
        time = watch.toString(Qt.DefaultLocaleLongDate)
        print(time)
        self.leave_line.setText(f'{time}')
        self.cursor.execute(f"update check_list set 퇴실시간 = '{time}' where 이름 = '{self.login[1]}'")
        self.db.commit()
        print(time)

    def outing_f(self):
        watch = QTime.currentTime()
        time = watch.toString(Qt.DefaultLocaleLongDate)
        self.outing_line.setText(f'{time}')
        print(time)

    def comeback_f(self):
        watch = QTime.currentTime()
        time = watch.toString(Qt.DefaultLocaleLongDate)
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

    def calendarlist_del(self):
        self.cursor.execute(f"SELECT distinct * FROM check.message_date WHERE 이름 = '{self.login[1]}'")
        result = self.cursor.fetchall()
        self.date_list.setRowCount(len(result))
        self.date_list.setColumnCount(len(result[0]))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.date_list.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.date_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.cursor.execute(f"delete from check.message_date where 날짜 = '{self.cellchoice}'")
        self.db.commit()



    def calendarlist_update(self):
        pass


    def calendarlist_lookup(self):

        self.cursor.execute(f"SELECT distinct * FROM check.message_date WHERE 이름 = '{self.login[1]}'")
        result = self.cursor.fetchall()
        self.date_list.setRowCount(len(result))
        self.date_list.setColumnCount(len(result[0]))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.date_list.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.date_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)






# 수강평 -----------------------------------------------


if __name__ == "__main__" :

    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

