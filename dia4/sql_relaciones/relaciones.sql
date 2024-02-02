-- Active: 1706834553841@@127.0.0.1@3306@asistencia
CREATE TABLE IF NOT EXISTS alumno(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    email  VARCHAR(200),
    nota DOUBLE DEFAULT 0
);

CREATE TABLE IF NOT EXISTS asistencia(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    alumno_id INT NOT NULL,
    fecha_asistencia DATE NOT NULL,
    asistio TINYINT DEFAULT 1,
    FOREIGN KEY(alumno_id) REFERENCES alumno(id)
);

insert into alumno(nombre,email) values
('CESAR MAYTA','cesar@gmail.com'),
('LUIS PEREZ','luis@gmail.com'),
('CLAUDIA MARIN','claudia@gmail.com'),
('ROBERTO TORRES','roberto@gmail.com'),
('CARLA LOPEZ','carla@gmail.com');

select * from alumno

truncate table asistencia;

insert into asistencia(alumno_id,fecha_asistencia,asistio)
VALUES
(1,CURDATE(),1),
(2,CURDATE(),0),
(3,CURDATE(),1),
(4,CURDATE(),0),
(5,CURDATE(),1);

insert into asistencia(alumno_id,fecha_asistencia,asistio)
VALUES
(1,'2024-01-02',1),
(2,'2024-01-02',1),
(3,'2024-01-02',1),
(4,'2024-01-02',1),
(5,'2024-01-02',1);


select * from asistencia;
