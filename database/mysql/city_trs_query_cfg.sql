/* transaction city config */
--
-- Table structure for table `restaurant_bankcard`
--

DROP TABLE IF EXISTS `city_transaction_query_config`;
CREATE TABLE `city_transaction_query_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_id` int(11) NOT NULL,
  `date_from` TIMESTAMP NOT NULL,
  `date_end` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `city_id` (`city_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
