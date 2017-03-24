CREATE DATABASE acme_store;

use database acme_store;

CREATE TABLE productos(
	id_producto int(2) NOT NULL,
	productos varchar(20) NOT NULL,
	descripcion varchar(20) NOT NULL,
	existencias float NOT NULL,
	precio_compra float NOT NULL,
	precio_venta float NOT NULL
	primary key (id_producto)
);

insert into productos values ("1","Control","Xbox One","10","750","1000");
insert into productos values ("2","Bocina","Kaiser","5","2100","3000");
insert into productos values ("3","Memoria",USB 8GB","100","65","120");


