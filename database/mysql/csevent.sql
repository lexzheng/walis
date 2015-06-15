--
-- Table structure for table `cs_event`
--

DROP TABLE IF EXISTS `cs_event`;
CREATE TABLE `cs_event` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL COMMENT '报告人',
  `user_type` tinyint(4) DEFAULT NULL COMMENT '报告人类型',
  `user_info` varchar(64) DEFAULT NULL COMMENT '来电用户信息',
  `phone` varchar(64) NOT NULL,
  `priority` tinyint(4) NOT NULL DEFAULT 0,
  `source` tinyint(4) DEFAULT NULL COMMENT '来源',
  `status` tinyint(4) NOT NULL DEFAULT 0,
  `creater_id` int(11) NOT NULL COMMENT '事件创建人',
  `handler_id` int(11) NOT NULL COMMENT '事件处理人',
  `is_order_related` tinyint(1) NOT NULL DEFAULT 0,
  `order_id` bigint(20) DEFAULT NULL,
  `is_to_compensate` tinyint(1) NOT NULL DEFAULT 0,
  `compensation` int(11) DEFAULT NULL,
  `category_l1` int(11) DEFAULT NULL,
  `category_l2` int(11) DEFAULT NULL,
  `category_l3` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  INDEX `index_phone_handler` (`phone`, `handler_id`),
  INDEX `index_handler` (`handler_id`),
  INDEX `index_user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

--
-- Table structure for table `cs_event_record`
--

DROP TABLE IF EXISTS `cs_event_record`;
CREATE TABLE `cs_event_record` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `status` tinyint(4) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX `event_id` (`event_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

--
-- Table structure for table `cs_event_category`
--

DROP TABLE IF EXISTS `cs_event_category`;
CREATE TABLE `cs_event_category` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(64) NOT NULL DEFAULT '',
  `is_valid` tinyint(4) NOT NULL DEFAULT 0
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
