-- Active: 1706834553841@@127.0.0.1@3306@asistencia
CREATE TABLE IF NOT EXISTS alumno(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    email  VARCHAR(200),
    nota DOUBLE DEFAULT 0
);

ALTER TABLE alumno DROP COLUMN nota;

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

CREATE TABLE curso(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
)

insert into curso(nombre)
VALUES ('PYTHON'),('JAVASCRIPT'),('MYSQL'),('HTML Y CSS'),('REACT');

select * from curso;

CREATE TABLE alumno_curso(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    curso_id INT NOT NULL,
    alumno_id INT NOT NULL,
    nota DOUBLE DEFAULT 0,
    FOREIGN KEY(curso_id) REFERENCES curso(id),
    FOREIGN KEY(alumno_id) REFERENCES alumno(id)
);

insert into alumno_curso(curso_id,alumno_id,nota)
VALUES
(1,1,20),(1,2,15),(1,3,11),(1,4,9),(1,5,17),
(2,1,11),(2,2,10),(2,4,19),(2,5,20),
(3,1,14),(3,2,13),(3,3,8),(3,4,20),(3,5,17),
(4,1,9),(4,2,16),(4,3,11),(4,5,20),
(5,1,19),(5,2,14),(5,3,12),(5,4,15),(5,5,17);
