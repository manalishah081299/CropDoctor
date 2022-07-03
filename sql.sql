/*
SQLyog Ultimate v11.11 (32 bit)
MySQL - 5.0.27-community-nt : Database - pythondb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pythondb` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pythondb`;

/*Table structure for table `classification_table` */

DROP TABLE IF EXISTS `classification_table`;

CREATE TABLE `classification_table` (
  `classification_id` int(11) NOT NULL auto_increment,
  `classification_login_id` int(11) default NULL,
  `classification_crop_id` int(11) default NULL,
  `classification_disease_id` int(11) default NULL,
  `classification_imagename` varchar(255) NOT NULL,
  `classification_imagepath` varchar(255) NOT NULL,
  `classification_status` varchar(255) NOT NULL,
  `classification_datetime` datetime default NULL,
  PRIMARY KEY  (`classification_id`),
  KEY `classification_login_id` (`classification_login_id`),
  KEY `classification_crop_id` (`classification_crop_id`),
  KEY `classification_disease_id` (`classification_disease_id`),
  CONSTRAINT `classification_table_ibfk_1` FOREIGN KEY (`classification_login_id`) REFERENCES `login_table` (`login_id`),
  CONSTRAINT `classification_table_ibfk_2` FOREIGN KEY (`classification_crop_id`) REFERENCES `crop_table` (`crop_id`),
  CONSTRAINT `classification_table_ibfk_3` FOREIGN KEY (`classification_disease_id`) REFERENCES `disease_table` (`disease_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `classification_table` */

insert  into `classification_table`(`classification_id`,`classification_login_id`,`classification_crop_id`,`classification_disease_id`,`classification_imagename`,`classification_imagepath`,`classification_status`,`classification_datetime`) values (1,9,7,2,'00e909aa-e3ae-4558-9961-336bb0f35db3___JR_FrgE.S_8593.JPG','../static/adminResources/input_image/','Apple___Black_rot','2021-04-07 18:42:59'),(8,9,6,4,'0a11f9e8-7357-48c2-8550-daeae59a1e76___RS_NLB_3588.JPG','../static/adminResources/input_image/','Corn_(maize)___Northern_Leaf_Blight','2021-04-08 10:47:58'),(9,9,6,12,'RS_Rust_1565.JPG','../static/adminResources/input_image/','Corn_(maize)___Common_rust_','2021-04-08 10:51:46'),(10,9,7,2,'0b37761a-de32-47ee-a3a4-e138b97ef542___JR_FrgE.S_2908.JPG','../static/adminResources/input_image/','Apple___Black_rot','2021-04-08 11:48:42'),(11,9,6,4,'0a11f9e8-7357-48c2-8550-daeae59a1e76___RS_NLB_3588.JPG','../static/adminResources/input_image/','Corn_(maize)___Northern_Leaf_Blight','2021-04-08 11:49:49'),(12,9,6,4,'0a11f9e8-7357-48c2-8550-daeae59a1e76___RS_NLB_3588.JPG','../static/adminResources/input_image/','Corn_(maize)___Northern_Leaf_Blight','2021-04-08 11:50:38'),(13,9,7,3,'0ce943e7-3fed-41cb-8430-0e0f54ff2bc4___FREC_C.Rust_0014.JPG','../static/adminResources/input_image/','Apple___Cedar_apple_rust','2021-05-28 17:14:30'),(14,7,7,3,'1a80b84d-1a5a-4e23-8deb-823ba928e29a___FREC_C.Rust_4431.JPG','../static/adminResources/input_image/','Apple___Cedar_apple_rust','2021-05-28 17:54:25');

/*Table structure for table `complain_table` */

DROP TABLE IF EXISTS `complain_table`;

CREATE TABLE `complain_table` (
  `complain_id` int(11) NOT NULL auto_increment,
  `complain_subject` varchar(255) NOT NULL,
  `complain_description` varchar(255) NOT NULL,
  `complain_datetime` datetime default NULL,
  `complain_status` varchar(20) default NULL,
  `complain_from_login_id` int(11) default NULL,
  `complain_to_login_id` int(11) default NULL,
  `complain_reply_description` varchar(255) default NULL,
  `complain_reply_datetime` datetime default NULL,
  PRIMARY KEY  (`complain_id`),
  KEY `complain_from_login_id` (`complain_from_login_id`),
  KEY `complain_to_login_id` (`complain_to_login_id`),
  CONSTRAINT `complain_table_ibfk_1` FOREIGN KEY (`complain_from_login_id`) REFERENCES `login_table` (`login_id`),
  CONSTRAINT `complain_table_ibfk_2` FOREIGN KEY (`complain_to_login_id`) REFERENCES `login_table` (`login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complain_table` */

insert  into `complain_table`(`complain_id`,`complain_subject`,`complain_description`,`complain_datetime`,`complain_status`,`complain_from_login_id`,`complain_to_login_id`,`complain_reply_description`,`complain_reply_datetime`) values (16,'xyzdfvd','ewrfgtthyd','2021-04-07 22:29:25','Replied',9,1,'we will solve soon','2021-04-07 22:30:43'),(17,'worst abc','very bad','2021-04-08 11:53:21','Replied',9,1,'we will solve soon','2021-04-08 11:54:30');

/*Table structure for table `crop_table` */

DROP TABLE IF EXISTS `crop_table`;

CREATE TABLE `crop_table` (
  `crop_id` int(11) NOT NULL auto_increment,
  `crop_name` varchar(255) NOT NULL,
  `crop_description` varchar(255) NOT NULL,
  PRIMARY KEY  (`crop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `crop_table` */

insert  into `crop_table`(`crop_id`,`crop_name`,`crop_description`) values (6,'Vegetable','vegetables are tomato,potato'),(7,'Fruit','Fruits are mango,papaya'),(8,'Pulses','Pulses xyzzz abc\r\n                                                      ');

/*Table structure for table `dataset_table` */

DROP TABLE IF EXISTS `dataset_table`;

CREATE TABLE `dataset_table` (
  `dataset_id` int(11) NOT NULL auto_increment,
  `dataset_disease_id` int(11) default NULL,
  `dataset_description` varchar(255) NOT NULL,
  `dataset_imagename` varchar(255) NOT NULL,
  `dataset_imagepath` varchar(255) NOT NULL,
  `dataset_datetime` datetime default NULL,
  PRIMARY KEY  (`dataset_id`),
  KEY `dataset_disease_id` (`dataset_disease_id`),
  CONSTRAINT `dataset_table_ibfk_1` FOREIGN KEY (`dataset_disease_id`) REFERENCES `disease_table` (`disease_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dataset_table` */

insert  into `dataset_table`(`dataset_id`,`dataset_disease_id`,`dataset_description`,`dataset_imagename`,`dataset_imagepath`,`dataset_datetime`) values (1,7,'image','0bdc5e46-cdfc-4e14-910a-dbdb3841634d___FAM_L.Blight_4784.JPG','../static/adminResources/dataset/','2021-04-08 11:47:24');

/*Table structure for table `disease_table` */

DROP TABLE IF EXISTS `disease_table`;

CREATE TABLE `disease_table` (
  `disease_id` int(11) NOT NULL auto_increment,
  `disease_name` varchar(255) NOT NULL,
  `disease_description` varchar(255) NOT NULL,
  `disease_crop_id` int(11) default NULL,
  PRIMARY KEY  (`disease_id`),
  KEY `disease_crop_id` (`disease_crop_id`),
  CONSTRAINT `disease_table_ibfk_1` FOREIGN KEY (`disease_crop_id`) REFERENCES `crop_table` (`crop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `disease_table` */

insert  into `disease_table`(`disease_id`,`disease_name`,`disease_description`,`disease_crop_id`) values (1,'Apple___Apple_scab','Apple___Apple_scab\r\n',7),(2,'Apple___Black_rot','Apple___Black_rot',7),(3,'Apple___Cedar_apple_rust','Apple___Cedar_apple_rust',7),(4,'Corn_(maize)___Northern_Leaf_Blight','Corn_(maize)___Northern_Leaf_Blight',6),(5,'Grape___Black_rot','Grape___Black_rot',7),(6,'Grape___Esca_(Black_Measles)','Grape___Esca_(Black_Measles)',7),(7,'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',7),(8,'Orange___Haunglongbing_(Citrus_greening)','Orange___Haunglongbing_(Citrus_greening)\r\n',7),(9,'Peach___Bacterial_spot','Peach___Bacterial_spot',7),(10,'Pepper,_bell___Bacterial_spot','Pepper,_bell___Bacterial_spot',7),(11,'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot is a vegetable disease',6),(12,'Corn_(maize)___Common_rust_','Corn_(maize)___Common_rust_ is a vegetable disease',6),(13,'rotten','very bad condition',7);

/*Table structure for table `feedback_table` */

DROP TABLE IF EXISTS `feedback_table`;

CREATE TABLE `feedback_table` (
  `feedback_id` int(11) NOT NULL auto_increment,
  `feedback_description` varchar(255) NOT NULL,
  `feedback_rating` int(11) NOT NULL,
  `feedback_datetime` datetime default NULL,
  `feedback_login_id` int(11) default NULL,
  PRIMARY KEY  (`feedback_id`),
  KEY `feedback_login_id` (`feedback_login_id`),
  CONSTRAINT `feedback_table_ibfk_1` FOREIGN KEY (`feedback_login_id`) REFERENCES `login_table` (`login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback_table` */

insert  into `feedback_table`(`feedback_id`,`feedback_description`,`feedback_rating`,`feedback_datetime`,`feedback_login_id`) values (17,'worstttt',3,'2021-04-07 22:29:48',9);

/*Table structure for table `login_table` */

DROP TABLE IF EXISTS `login_table`;

CREATE TABLE `login_table` (
  `login_id` int(11) NOT NULL auto_increment,
  `login_username` varchar(255) NOT NULL,
  `login_password` varchar(255) NOT NULL,
  `login_role` varchar(255) NOT NULL,
  `login_status` varchar(255) NOT NULL,
  `login_secretkey` varchar(255) NOT NULL,
  PRIMARY KEY  (`login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login_table` */

insert  into `login_table`(`login_id`,`login_username`,`login_password`,`login_role`,`login_status`,`login_secretkey`) values (1,'shah.minu99@gmail.com','admin12345','admin','active','hMaES&2w!2jx?S6TGy65ScJk7upY?t99'),(7,'manalithakkar735@gmail.com','hppQu6z3','user','active','myQ8WHMNA3kUIL0T3PS3ow2vbpSgjPln'),(9,'shah.manaliv99@gmail.com','pd89hDsJ','user','active','Fc3RxFW5lq8P77js3wvmgh6yW1uuADAe');

/*Table structure for table `medicine_table` */

DROP TABLE IF EXISTS `medicine_table`;

CREATE TABLE `medicine_table` (
  `medicine_id` int(11) NOT NULL auto_increment,
  `medicine_name` varchar(255) NOT NULL,
  `medicine_crop_id` int(11) default NULL,
  `medicine_disease_id` int(11) default NULL,
  PRIMARY KEY  (`medicine_id`),
  KEY `medicine_crop_id` (`medicine_crop_id`),
  KEY `medicine_disease_id` (`medicine_disease_id`),
  CONSTRAINT `medicine_table_ibfk_1` FOREIGN KEY (`medicine_crop_id`) REFERENCES `crop_table` (`crop_id`),
  CONSTRAINT `medicine_table_ibfk_2` FOREIGN KEY (`medicine_disease_id`) REFERENCES `disease_table` (`disease_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `medicine_table` */

/*Table structure for table `user_table` */

DROP TABLE IF EXISTS `user_table`;

CREATE TABLE `user_table` (
  `user_id` int(11) NOT NULL auto_increment,
  `user_firstname` varchar(255) NOT NULL,
  `user_lastname` varchar(255) NOT NULL,
  `user_gender` varchar(255) NOT NULL,
  `user_address` varchar(255) NOT NULL,
  `user_contact` int(11) NOT NULL,
  `user_login_id` int(11) default NULL,
  PRIMARY KEY  (`user_id`),
  KEY `user_login_id` (`user_login_id`),
  CONSTRAINT `user_table_ibfk_1` FOREIGN KEY (`user_login_id`) REFERENCES `login_table` (`login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_table` */

insert  into `user_table`(`user_id`,`user_firstname`,`user_lastname`,`user_gender`,`user_address`,`user_contact`,`user_login_id`) values (3,'manali','Thakkar','Female','efgrth',1234567890,7),(5,'shreya','patel','Female','1tjy',1234567890,9);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
