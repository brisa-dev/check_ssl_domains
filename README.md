# Check SSL Domains
Extract SSL data from domains

### Environments
```shell
export MYSQL_HOST=mysql_host
export MYSQL_USER=mysql_user
export MYSQL_PASS=mysql_user_password
export MYSQL_DATABASE=mysql_database_name
```

### Database estructure
```sql
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
```

### How to use
To input data into database
```shell
python3 run.py --insert-to-database
```