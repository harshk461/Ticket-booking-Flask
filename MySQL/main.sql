-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: railway
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cancellation_detail`
--

DROP TABLE IF EXISTS `cancellation_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancellation_detail` (
  `CANCEL_ID` varchar(20) NOT NULL,
  `PNR` varchar(20) DEFAULT NULL,
  `NAME` varchar(500) DEFAULT NULL,
  `AGE` varchar(100) DEFAULT NULL,
  `GENDER` varchar(100) DEFAULT NULL,
  `TRAIN_NAME` varchar(100) DEFAULT NULL,
  `STATUS` varchar(100) DEFAULT NULL,
  `NO_CANCELLED_PASSNG` varchar(10) DEFAULT NULL,
  `DATE_CANCEL` varchar(20) DEFAULT NULL,
  `berth` varchar(100) DEFAULT NULL,
  `seat` varchar(100) DEFAULT NULL,
  `food` varchar(100) DEFAULT NULL,
  `coach` varchar(100) DEFAULT NULL,
  `class` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CANCEL_ID`),
  UNIQUE KEY `PNR` (`PNR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancellation_detail`
--

LOCK TABLES `cancellation_detail` WRITE;
/*!40000 ALTER TABLE `cancellation_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `cancellation_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distance`
--

DROP TABLE IF EXISTS `distance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distance` (
  `train_no` int DEFAULT NULL,
  `distance` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distance`
--

LOCK TABLES `distance` WRITE;
/*!40000 ALTER TABLE `distance` DISABLE KEYS */;
INSERT INTO `distance` VALUES (12280,300),(18098,300),(12534,1200),(18768,1200),(13298,300),(16273,1400),(16213,1400),(13213,1200),(18783,1400);
/*!40000 ALTER TABLE `distance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `journey_det`
--

DROP TABLE IF EXISTS `journey_det`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `journey_det` (
  `PNR` varchar(40) NOT NULL,
  `transaction` varchar(40) DEFAULT NULL,
  `date_of_book` varchar(20) DEFAULT NULL,
  `date_jour` varchar(20) DEFAULT NULL,
  `start` varchar(40) DEFAULT NULL,
  `end` varchar(40) DEFAULT NULL,
  `mobile_no` varchar(15) DEFAULT NULL,
  `train_name` varchar(50) DEFAULT NULL,
  `train_no` varchar(50) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `user` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`PNR`),
  UNIQUE KEY `transaction` (`transaction`),
  CONSTRAINT `journey_det_ibfk_1` FOREIGN KEY (`PNR`) REFERENCES `passenger` (`PNR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `journey_det`
--

LOCK TABLES `journey_det` WRITE;
/*!40000 ALTER TABLE `journey_det` DISABLE KEYS */;
INSERT INTO `journey_det` VALUES ('2839549576','CB2503651065',' 2020-06-27','2020-06-28','DEL','AGR','','TAJ EXPRESS','12280','Confirmed',NULL),('3803255269','CC2030114344',' 2020-06-29','2020-12-31','DEL','AGR','','TAJ EXPRESS','12280','Confirmed',NULL),('7617088598','GH6457149611',' 2020-06-29','2020-12-31','DEL','AGR','12345','TAJ EXPRESS','12280','Confirmed',NULL);
/*!40000 ALTER TABLE `journey_det` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `user` varchar(10) NOT NULL,
  `passward` varchar(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `mail` varchar(30) DEFAULT NULL,
  `phone_no` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger`
--

DROP TABLE IF EXISTS `passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger` (
  `passng` varchar(400) DEFAULT NULL,
  `age` varchar(30) DEFAULT NULL,
  `gen` varchar(30) DEFAULT NULL,
  `BRTH` varchar(300) DEFAULT NULL,
  `seat` varchar(40) DEFAULT NULL,
  `food` varchar(40) DEFAULT NULL,
  `price` float(12,2) DEFAULT NULL,
  `PNR` varchar(40) NOT NULL,
  `coach` varchar(10) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `user` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`PNR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger`
--

LOCK TABLES `passenger` WRITE;
/*!40000 ALTER TABLE `passenger` DISABLE KEYS */;
INSERT INTO `passenger` VALUES ('Harsh,','17,','Male,','Upper Berth,','87,','Veg,',280.00,'2839549576','D2','SL',NULL),('Qwert 123,','17,','Male,','Upper Berth,','98,','Veg,',280.00,'3803255269','D4','SL',NULL),('Qwert 123,','17,','Male,','Upper Berth,','94,','Veg,',280.00,'7617088598','D2','SL',NULL);
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rail`
--

DROP TABLE IF EXISTS `rail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rail` (
  `START` varchar(20) DEFAULT NULL,
  `FROM_CODE` varchar(10) DEFAULT NULL,
  `END` varchar(20) DEFAULT NULL,
  `TO_CODE` varchar(10) DEFAULT NULL,
  `TRAIN_NO` int DEFAULT NULL,
  `TRAIN_NAME` varchar(30) DEFAULT NULL,
  `ARR_TIME` varchar(10) DEFAULT NULL,
  `DEPT_TIME` varchar(10) DEFAULT NULL,
  `TIME_PERIOD` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rail`
--

LOCK TABLES `rail` WRITE;
/*!40000 ALTER TABLE `rail` DISABLE KEYS */;
INSERT INTO `rail` VALUES ('DELHI','DEL','AGRA','AGR',12280,'TAJ EXPRESS','7:10','10:05','2H 55M'),('DELHI','DEL','MUMBAI','BCT',12534,'DEL-BCT EXP','10:10','10:20','12H 10M'),('DELHI','DEL','MUMBAI','BCT',18768,'BCT-DEL EXP','23:30','23:50','12H 20M'),('DELHI','DEL','AGRA','AGR',18098,'AGR-DEL EXP','13:30','13:50','12H 20M'),('AGRA','AGR','MUMBAI','BCT',16273,'AGR-BCT EXP','15:20','16:20','12H 10M'),('AGRA','AGR','MUMBAI','BCT',16213,'AGR-BOM EXP','16:20','17:20','12H 10M'),('MUMBAI','BCT','DELHI','DEL',13213,'BOM-DEL EXP','16:20','17:20','12H 10M'),('JAIPUR','JAP','DELHI','DEL',12113,'JAP-DEL EXP','16:20','17:20','12H 10M'),('DELHI','DEL','JAIPUR','JAP',12323,'DEL-JAP EXP','10:20','14:20','4H 0M');
/*!40000 ALTER TABLE `rail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-29 17:29:35
