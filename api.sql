DROP DATABASE IF EXISTS `apidabase`;
CREATE DATABASE IF NOT EXISTS `apidabase`
USE `apidabase`;

DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT EXISTS `employees` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(40) DEFAULT NULL,
  `Edad` varchar(40) DEFAULT NULL,
  `Telefono` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `employees` (`id`, `Nombre`, `Edad`, `Telefono`) VALUES
	(1, 'Juan', '15', '12340987'),
	(2, 'Maria', '20', '1777787'),
	(3, 'Ana', '33', '44448888'),
	(4, 'Juan', '33', '3333'),
	(6, 'Paul', '33', '3333'),
	(7, 'Tail', '33', '3333'),
	(8, 'Sonic', '33', '3333'),
	(9, 'Sonic', '', '3333');
