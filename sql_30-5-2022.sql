/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - 22_house_price
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`22_house_price` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `22_house_price`;

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(89) DEFAULT NULL,
  `password` varchar(90) DEFAULT NULL,
  `usertype` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'j@gmail.com','1234','user'),(3,'a@gmail.com','1234','user'),(4,'y@gmail.com','1234','user'),(5,'ak@gmail.com','1234','user'),(6,'ashwin01@gmail.com','1234','user');

/*Table structure for table `property` */

DROP TABLE IF EXISTS `property`;

CREATE TABLE `property` (
  `property_id` int(11) NOT NULL AUTO_INCREMENT,
  `zone` varchar(90) DEFAULT NULL,
  `lotfrontage` varchar(90) DEFAULT NULL,
  `lotarea` varchar(90) DEFAULT NULL,
  `street_type` varchar(90) DEFAULT NULL,
  `alley_type` varchar(90) DEFAULT NULL,
  `lotshape` varchar(90) DEFAULT NULL,
  `utilities` varchar(90) DEFAULT NULL,
  `housestyle` varchar(90) DEFAULT NULL,
  `yearbuild` varchar(80) DEFAULT NULL,
  `bedroom` varchar(89) DEFAULT NULL,
  `kitchen` varchar(90) DEFAULT NULL,
  `price` varchar(90) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`property_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `property` */

insert  into `property`(`property_id`,`zone`,`lotfrontage`,`lotarea`,`street_type`,`alley_type`,`lotshape`,`utilities`,`housestyle`,`yearbuild`,`bedroom`,`kitchen`,`price`,`userid`) values (14,'Residential Low Density','60','2189','Pave','Pave','IR1:Slightly Irregular','All Public Utilities (E,G,W,& S)','2Story','2001','8','2','5768960',2),(15,'Residential Low Density','70','1500','Pave','3','Regular','All Public Utilities (E,G,W,& S)','1Story','2010','7','1','4890000',3),(16,'Residential Medium Density','50','5000','Pave','Grvl','Regular','All Public Utilities (E,G,W,& S)','1.5Story: 2nd level finished','2003','9','2','6780000',1),(17,'Floating Village Residential','64','2300','Grvl','Pave','Regular','NoSeWa :Electricity and Gas Only','Split Foyer','2004','7','2','5675000',1),(18,'Residential Low Density','47','3490','Pave','Pave','Regular','All Public Utilities (E,G,W,& S)','Split Lvl','2010','8','2','4938000',3),(19,'Commercial','64','5000','Pave','Pave','IR2: Moderately Irregular','All Public Utilities (E,G,W,& S)','2Story','2008','6','2','5000000',4),(20,'Residential High Density','68','2067','Pave','Pave','Regular','All Public Utilities (E,G,W,& S)','2.5Story: 2nd level finished','1989','7','3','5200000',4),(21,'Residential Medium Density','60','4100','Grvl','Grvl','IR1:Slightly Irregular','All Public Utilities (E,G,W,& S)','2Story','1998','8','2','5345000',5),(22,'Commercial','54','2100','Pave','Grvl','Regular','NoSeWa: Electricity and Gas Only','1Story','2010','6','1','5600000',6),(23,'Commercial','54','2100','Pave','Grvl','Regular','NoSeWa: Electricity and Gas Only','1Story','2010','6','1','2000000',6),(25,'Residential Medium Density','60','1700','Pave','Grvl','Regular','All Public Utilities (E,G,W,& S)','1Story','2012','4','1','3224425.0',3),(26,'Commercial','64','5000','Pave','Pave','Regular','All Public Utilities (E,G,W,& S)','1.5Story: 2nd level finished','2000','8','2','4123056.65',3);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(90) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `phone` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`name`,`email`,`phone`) values (2,'Joseph M J','j@gmail.com','9170343445'),(3,'Aswin Anirudhan','a@gmail.com','9947781769'),(4,'Yadu Krishnan','y@gmail.com','9856463616'),(5,'Akhil Jolly','ak@gmail.com','7561845100'),(6,'Ashwin','ashwin01@gmail.com','9744986752');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
