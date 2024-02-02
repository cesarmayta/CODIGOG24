-- Active: 1706834553841@@127.0.0.1@3306@asistencia
-- INNER JOIN
select a.nombre,s.fecha_asistencia,s.asistio FROM
alumno a inner join asistencia s on s.alumno_id = a.id;

-- LEFT JOIN
select curso.nombre,alumno_curso.nota 
from curso LEFT JOIN alumno_curso ON curso.id = alumno_curso.curso_id;

select * from curso;
delete from alumno_curso where curso_id = 5;

select alumno.nombre,avg(alumno_curso.nota)
from alumno_curso right join alumno on alumno_curso.alumno_id = alumno.id
group by alumno.nombre;

delete from alumno_curso where alumno_id = 4;