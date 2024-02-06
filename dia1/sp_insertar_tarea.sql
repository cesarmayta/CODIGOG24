-- Active: 1706834553841@@127.0.0.1@3306@api_rest
DROP PROCEDURE sp_insertar_tarea;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertar_tarea`(IN descripcion_value VARCHAR(250))
BEGIN
    insert into tarea(descripcion) values(descripcion_value);
    select id,descripcion,estado from tarea order by id desc limit 1;
END