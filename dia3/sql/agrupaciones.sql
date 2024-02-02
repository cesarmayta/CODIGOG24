-- Active: 1706753740285@@127.0.0.1@3306@contactos
truncate table contacto;
select * from contacto;

-- FUNCIONES DE AGRUPACIÓN;
-- TOTAL DE REGISTROS
select count(*) from contacto;
-- TOTAL DE REGISTROS POR PAIS
select pais,count(*) from contacto
group by pais
order by count(*) desc