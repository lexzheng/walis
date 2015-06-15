--
-- 表的结构 `region_brand`
--

CREATE TABLE IF NOT EXISTS `region_brand` (
`id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `type_code` tinyint(4) NOT NULL,
  `city_id` int(11) NOT NULL,
  `area` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `city_id` (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


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
-- Table structure for table `certification_processing_record`
--

DROP TABLE IF EXISTS `certification_processing_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `certification_processing_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
    `process_user_id` int(11) NOT NULL,
  `restaurant_id` int(11) NOT NULL,
    `certification_type` tinyint(4) NOT NULL,
  `status_from` tinyint(4) NOT NULL,
    `status_to` tinyint(4) NOT NULL,
  `comment` varchar(100) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
    KEY `process_user_id` (`process_user_id`,`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=213 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `payment_notice_record`
--

DROP TABLE IF EXISTS `payment_notice_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment_notice_record` (
  `record_id` int(11) NOT NULL AUTO_INCREMENT,
    `phone` varchar(32) NOT NULL DEFAULT '',
  `restaurant_id` int(11) DEFAULT NULL,
    `restaurant_name` varchar(64) DEFAULT NULL,
  `activity_name` varchar(64) DEFAULT NULL,
    `first_date` date DEFAULT NULL,
  `last_date` date DEFAULT NULL,
    `amount` int(11) DEFAULT NULL,
  `total_subsidy` decimal(10,2) DEFAULT NULL,
    `process_date` date DEFAULT NULL,
  `card_num_tail` varchar(32) DEFAULT NULL,
    `status` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `sms_task_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`record_id`),
    KEY `restaurant_id` (`restaurant_id`),
  KEY `created_at` (`created_at`),
    KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=253 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `payment_notice_reply`
--

DROP TABLE IF EXISTS `payment_notice_reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment_notice_reply` (
  `reply_id` int(11) NOT NULL,
    `phone_number` varchar(32) NOT NULL DEFAULT '',
  `message` varchar(255) DEFAULT '',
    `reply_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`reply_id`),
  KEY `phone_number` (`phone_number`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `region_principal`
--

DROP TABLE IF EXISTS `region_principal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `region_principal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
    `city_id` int(11) NOT NULL,
  `region_group_id` int(11) NOT NULL,
    `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
    KEY `city_id_region_group_id` (`city_id`,`region_group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `restaurant_info_notification`
--

DROP TABLE IF EXISTS `restaurant_info_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurant_info_notification` (
  `id` int(11) NOT NULL,
    `restaurant_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
    `notice_enabled` smallint(6) NOT NULL,
  `in_charge` smallint(6) NOT NULL,
    `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `restaurant_recruitment`
--

DROP TABLE IF EXISTS `restaurant_recruitment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurant_recruitment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
    `restaurant_id` int(11) NOT NULL DEFAULT '0',
  `headcount` int(11) NOT NULL DEFAULT '0',
    `salary` decimal(10,2) NOT NULL DEFAULT '0.00',
  `working_time_start` time DEFAULT NULL,
    `working_time_end` time DEFAULT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '0',
    `comment` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `city_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_register_info`
--

DROP TABLE IF EXISTS `user_register_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_register_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(16) NOT NULL DEFAULT '',
    `email` varchar(64) NOT NULL DEFAULT '',
  `mobile` varchar(16) NOT NULL DEFAULT '',
    `city` varchar(8) NOT NULL DEFAULT '',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `voice_call`
--

DROP TABLE IF EXISTS `voice_call`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `voice_call` (
  `id` int(11) NOT N) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `voicecall_ban`
--

DROP TABLE IF EXISTS `voicecall_ban`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `voicecall_ban` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
    `restaurant_id` int(11) NOT NULL DEFAULT '0',
  `ban_type` tinyint(4) NOT NULL DEFAULT '0',
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@
