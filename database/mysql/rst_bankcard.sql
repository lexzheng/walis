/* bankcard bind */
--
-- Table structure for table `restaurant_bankcard`
--

DROP TABLE IF EXISTS `restaurant_bankcard`;
CREATE TABLE `restaurant_bankcard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_code` tinyint(4) NOT NULL DEFAULT 0,
  `status` tinyint(4) NOT NULL DEFAULT 0,
  `rst_id` int(11) NOT NULL,
  `username` varchar(64) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `bank_id` tinyint(4) NOT NULL,
  `card_id` varchar(32) NOT NULL,
  `cardholder_name` varchar(64) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `comment` varchar(100) DEFAULT '''''',
  `bankcard_image_front` varchar(128) DEFAULT NULL,
  `identity_card_image_front` varchar(128) DEFAULT NULL,
  `identity_card_image_back` varchar(128) DEFAULT NULL,
  `ol_pay_contract_image` varchar(128) DEFAULT NULL,
  `misc_image` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  INDEX `rst_id` (`rst_id`),
  INDEX `status` (`status`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

--
-- Table structure for table `restaurant_bankcard_processing_record`
--

DROP TABLE IF EXISTS `restaurant_bankcard_processing_record`;
CREATE TABLE `restaurant_bankcard_processing_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rst_id` int(11) NOT NULL,
  `bankcard_id` int(11) NOT NULL,
  `process_user_id` int(11) NOT NULL,
  `messages` varchar(100) DEFAULT NULL,
  `status_to` tinyint(4) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  INDEX `bankcard_id` (`bankcard_id`),
  INDEX `rst_id` (`rst_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
