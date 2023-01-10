-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: check
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `check_list`
--

DROP TABLE IF EXISTS `check_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `check_list` (
  `번호` int DEFAULT NULL,
  `이름` varchar(45) DEFAULT NULL,
  `아이디` varchar(45) DEFAULT NULL,
  `비밀번호` int DEFAULT NULL,
  `입실시간` varchar(45) DEFAULT NULL,
  `퇴실시간` varchar(45) DEFAULT NULL,
  `출석여부` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_list`
--

LOCK TABLES `check_list` WRITE;
/*!40000 ALTER TABLE `check_list` DISABLE KEYS */;
INSERT INTO `check_list` VALUES (1,'강민영','kmy',1234,NULL,NULL,NULL),(2,'고연재','kyj',1234,NULL,NULL,NULL),(3,'김기태','kkt',1234,NULL,NULL,NULL),(4,'김명은','kmy',1234,NULL,NULL,NULL),(5,'김성일','ksi',1234,NULL,NULL,NULL),(6,'김연수','kys',1234,NULL,NULL,NULL),(7,'노도현','ndh',1234,NULL,NULL,NULL),(8,'류가미','rgm',1234,NULL,NULL,NULL),(9,'박규환','pgh',1234,NULL,NULL,NULL),(10,'박성빈','psb',1234,NULL,NULL,NULL),(11,'박시형','psh',1234,NULL,NULL,NULL),(12,'박의용','pyy',1234,NULL,NULL,NULL),(13,'오송화','osh',1234,'2023-01-10 14:51:17','2023-01-10 14:51:18',NULL),(14,'이범규','lbg',1234,NULL,NULL,NULL),(15,'이보라','lbr',1234,'오후 4:07:52','오후 4:07:54',NULL),(16,'이소윤','lsy',1234,NULL,NULL,NULL),(17,'이여름','lyr',1234,NULL,NULL,NULL),(18,'이지혜','ljy',1234,NULL,NULL,NULL),(19,'이현도','lhd',1234,NULL,NULL,NULL),(20,'임성경','isg',1234,NULL,NULL,NULL),(21,'임영효','iyh',1234,NULL,NULL,NULL),(22,'임홍선','ihs',1234,NULL,NULL,NULL),(23,'장은희','jyh',1234,NULL,NULL,NULL),(24,'정연우','jyy',1234,NULL,NULL,NULL),(25,'정철우','jcy',1234,NULL,NULL,NULL),(26,'주민석','jms',1234,NULL,NULL,NULL),(27,'최지혁','cjh',1234,NULL,NULL,NULL),(21,'임영효','iyh',1234,NULL,NULL,NULL);
/*!40000 ALTER TABLE `check_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-10 16:42:47
