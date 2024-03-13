CREATE TABLE IF NOT EXISTS `tarea` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(200) NOT NULL,
  `estado` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla db_tareas.tarea: ~4 rows (aproximadamente)
INSERT INTO `tarea` (`id`, `descripcion`, `estado`) VALUES
	(1, 'tarea 1', 'pendiente'),
	(2, 'tarea 2', 'pendiente');