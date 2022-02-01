CREATE TABLE `ssl_domains_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer` varchar(45) DEFAULT NULL,
  `domain` varchar(200) DEFAULT NULL,
  `notAfter` datetime DEFAULT NULL,
  `status` int DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;