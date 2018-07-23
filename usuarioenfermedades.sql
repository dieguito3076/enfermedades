-- MySQL dump 10.13  Distrib 5.7.17, for Win32 (AMD64)
--
-- Host: localhost    Database: usuarioenfermedades
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lecturaspulso`
--

DROP TABLE IF EXISTS `lecturaspulso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lecturaspulso` (
  `userKey` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `lectura` float unsigned NOT NULL,
  PRIMARY KEY (`userKey`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=ascii COLLATE=ascii_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lecturaspulso`
--

LOCK TABLES `lecturaspulso` WRITE;
/*!40000 ALTER TABLE `lecturaspulso` DISABLE KEYS */;
INSERT INTO `lecturaspulso` VALUES (1,54),(2,54.02),(3,54.4),(4,54.7),(5,54.8),(6,54.89),(7,55),(8,56),(9,60),(10,60),(11,60),(12,60),(13,60),(14,61),(15,61),(16,60),(17,60),(18,60),(19,60),(20,60);
/*!40000 ALTER TABLE `lecturaspulso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lecturasresp`
--

DROP TABLE IF EXISTS `lecturasresp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lecturasresp` (
  `userKey` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `lectura` float unsigned NOT NULL,
  PRIMARY KEY (`userKey`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=ascii COLLATE=ascii_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lecturasresp`
--

LOCK TABLES `lecturasresp` WRITE;
/*!40000 ALTER TABLE `lecturasresp` DISABLE KEYS */;
INSERT INTO `lecturasresp` VALUES (1,11.1),(2,11.1),(3,11.1),(4,11.1),(5,11.4),(6,11.6),(7,11.6),(8,11.6),(9,11.6),(10,11.8),(11,11.9),(12,11.9),(13,11.9),(14,12),(15,12),(16,12),(17,12),(18,12),(19,12),(20,12);
/*!40000 ALTER TABLE `lecturasresp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lecturastemp`
--

DROP TABLE IF EXISTS `lecturastemp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lecturastemp` (
  `userKey` int(4) NOT NULL AUTO_INCREMENT,
  `lectura` float unsigned DEFAULT NULL,
  PRIMARY KEY (`userKey`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=ascii COLLATE=ascii_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lecturastemp`
--

LOCK TABLES `lecturastemp` WRITE;
/*!40000 ALTER TABLE `lecturastemp` DISABLE KEYS */;
INSERT INTO `lecturastemp` VALUES (1,34),(2,34.26),(3,34.28),(4,34.3),(5,34.3),(6,34.33),(7,34.37),(8,34.39),(9,34.4),(10,34.45),(11,34.7),(12,34.7),(13,34.7),(14,34.7),(15,34.71),(16,34.73),(17,34.73),(18,34.76),(19,34.81),(20,34.81),(21,34.81),(22,34.81),(23,34.82),(24,34.88),(25,34.9),(26,35),(27,35),(28,35.01),(29,35.1),(30,35.3),(31,35.3),(32,35.5),(33,35.59),(34,35.8),(35,35.8),(36,35.9),(37,35.95),(38,35.99),(39,36),(40,36.01),(41,36.02),(42,36.1),(43,36.2),(44,36.3),(45,36.3),(46,36.4),(47,36.6),(48,36.6);
/*!40000 ALTER TABLE `lecturastemp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarioe`
--

DROP TABLE IF EXISTS `usuarioe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarioe` (
  `usuarioKey` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cadenaVal` varchar(70) COLLATE ascii_bin DEFAULT '000000000000000',
  `Edad` int(2) unsigned DEFAULT '0',
  `Peso` float unsigned DEFAULT '0',
  PRIMARY KEY (`usuarioKey`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=ascii COLLATE=ascii_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarioe`
--

LOCK TABLES `usuarioe` WRITE;
/*!40000 ALTER TABLE `usuarioe` DISABLE KEYS */;
INSERT INTO `usuarioe` VALUES (1,'0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',0,0);
/*!40000 ALTER TABLE `usuarioe` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-23  0:55:31
