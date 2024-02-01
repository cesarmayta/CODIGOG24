-- Active: 1706753740285@@127.0.0.1@3306@contactos
-- SENTENCIAS DML 
-- CRUD ( CREATE READ UPDATE DELETE)
-- CREATE : INSERT
insert into contacto(nombre,email) values('CESAR MAYTA','cesar@gmail.com');
insert into contacto(nombre,email,pais) values('ANA GARCIA','anita@gmail.com','Colombia');
insert into contacto(nombre,email)
VALUES
('LUIS PERES','luchito@hotmail.com'),
('SOFIA LOPEZ','sofy12@yahoo.es'),
('CARLOS SANTANDER','csantander@banco.com.pe');

-- READ : SELECT
select * from contacto;
select nombre from contacto;
select DISTINCT pais from contacto;

-- FILTROS
select * from contacto
where pais = 'Perú';
select * from contacto where id = 1;

-- UPDATE : UPDATE
update contacto
set pais = 'PERU';
update contacto
set pais = 'COLOMBIA'
where id = 2;

update contacto
set pais = 'PERÚ'
where pais = 'PERU';

-- DELETE : DELETE
delete from contacto
where id = 5;

select * from contacto;

insert into contacto(id,nombre,email) values(5,'JORGE SOTO','jorge@gmail.com');