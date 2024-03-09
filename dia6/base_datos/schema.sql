
create table user (
	id int not null auto_increment primary key,
	username varchar(50),
	name varchar(50),
	lastname varchar(50),
	email varchar(255),
	password varchar(60),
	is_active boolean not null default 1,
	kind int not null default 1,
	created_at datetime
);

insert into user (username,password,kind,is_active,created_at) value ("admin",sha1(md5("admin")),1,1,NOW());

create table project (
	id int not null auto_increment primary key,
	name varchar(200),
	description text
	);


create table category (
	id int not null auto_increment primary key,
	name varchar(200)
	);

create table kind (
	id int not null auto_increment primary key,
	name varchar(100)
);

insert into kind (id,name) values (1,"Ticket"), (2,"Bug"),(3,"Sugerencia"),(4,"Caracteristica");

create table subkind(
	id int not null auto_increment primary key,
	name varchar(100),
	kind_id int not null,
	foreign key (kind_id) references kind(id)
);

insert into subkind(name,kind_id)  values ("T1",1),("T2",1),("B1",2),("B2",2);

create table status (
	id int not null auto_increment primary key,
	name varchar(100)
);

insert into status (id,name) values (1,"Pendiente"), (2,"En Desarrollo"),(3,"Terminado"),(4,"Cancelado");

create table priority (
	id int not null auto_increment primary key,
	name varchar(100)
);

insert into priority (id,name) values  (1,"Alta"),(2,"Media"),(3,"Baja");



create table person(
	id int not null auto_increment primary key,
	code varchar(255),
	name varchar(255),
	lastname varchar(255),
	address varchar(255),
	email varchar(255),
	phone varchar(255),
	password varchar(60),
	image varchar(255),
	status int default 1,
	kind int default 1,
	created_at datetime
);


create table ticket(
	id int not null auto_increment primary key,
	code varchar(255),
	title varchar(100),
	description text,
	file varchar(255),
	file2 varchar(255),
	updated_at datetime,
	created_at datetime,
	kind_id int not null,
	subkind_id int,
	user_id int,
	person_id int,
	asigned_id int,
	project_id int,
	category_id int,
	priority_id int not null default 1,
	foreign key (priority_id) references priority(id),
	status_id int not null default 1,
	foreign key (status_id) references status(id),
	foreign key (asigned_id) references user(id),
	foreign key (person_id) references person(id),
	foreign key (user_id) references user(id),
	foreign key (kind_id) references kind(id),
	foreign key (subkind_id) references subkind(id),
	foreign key (category_id) references category(id) on delete cascade,
	foreign key (project_id) references project(id) on delete cascade
);

create table answer(
	id int not null auto_increment primary key,
	description text,
	file varchar(255),
	created_at datetime,
	user_id int,
	person_id int,
	status_id int default 1,
	ticket_id int not null default 1,
	kind int default 2, /* 1. predefined, 2. normal */
	foreign key (ticket_id) references ticket(id) on delete cascade,	
	foreign key (status_id) references status(id),	
	foreign key (user_id) references user(id)
);


create table history (
	id int not null auto_increment primary key,
	code varchar(50),
	date_at date,
	description varchar(500),
	status_id int default 1,
	created_at datetime,
	user_id int,
	asigned_id int,
	ticket_id int not null default 1,
	foreign key (status_id) references status(id),	
	foreign key (ticket_id) references ticket(id) on delete cascade,	
	foreign key (asigned_id) references user(id),
	foreign key (user_id) references user(id)
);


create table notification (
	id int not null auto_increment primary key,
	description text,
	created_at datetime,
	author_id int,
	receptor_id int,
	ticket_id int not null default 1,
	status int not null default 0,
	foreign key (ticket_id) references ticket(id) on delete cascade,	
	foreign key (author_id) references user(id),
	foreign key (receptor_id) references user(id)
);
