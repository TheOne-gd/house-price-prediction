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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'j@gmail.com','1234','user'),(3,'a@gmail.com','1234','user'),(4,'y@gmail.com','1234','user'),(5,'ak@gmail.com','1234','user');

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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `property` */

insert  into `property`(`property_id`,`zone`,`lotfrontage`,`lotarea`,`street_type`,`alley_type`,`lotshape`,`utilities`,`housestyle`,`yearbuild`,`bedroom`,`kitchen`,`price`,`userid`) values (1,'RM','60','1500','Pave','Pave','Reg','Allpub','1Story','1939','6','1','4500000',1),(2,'RL','60','1900','Pave','3','Reg','Allpub','1Story','2010','5','2','4500000',2),(3,'RL','50','1700','Pave','3','Reg','Allpub','2Story','2010','7','2','5000000',2),(4,'C(All)','70','8450','Pave','Grvl','IR1','Allpub','SFoyer','2003','10','2','7890000',3),(5,'RM','64','5643','Grvl','Grvl','Reg','NoSeWa','2Story','2008','5','1','4300000',3),(6,'FV','51','3769','Pave','Pave','IR2','Allpub','2.5Fin','2021','9','1','5000000',4),(7,'RH','53','2345','Pave','Grvl','IR1','NoSeWa','1.5Unf','2008','4','1','3450000',4),(8,'C(All)','76','6743','Grvl','Pave','Reg','Allpub','SLvl','2005','7','2','4670000',5),(9,'RH','51','5431','Pave','Pave','IR2','Allpub','1.5Unf','2012','8','3','5400000',5),(10,'RM','70','5450','Pave','Pave','IR2','Allpub','2.5Fin','2013','8','2','6700000',0),(11,'RL','78','6500','Pave','Pave','IR1','NoSeWa','2.5Unf','2020','6','2','7000000',1);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(90) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `phone` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`name`,`email`,`phone`) values (2,'Joseph M J','j@gmail.com','9170343445'),(3,'Aswin Anirudhan','a@gmail.com','9947781769'),(4,'Yadu Krishnan','y@gmail.com','9856463616'),(5,'Akhil Jolly','ak@gmail.com','7561845100');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
