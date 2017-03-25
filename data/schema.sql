CREATE DATABASE productos;

use database productos;

CREATE TABLE productoss(
	id_producto int(2) PRIMARY KEY NOT NULL,
	productos varchar(20) NOT NULL,
	descripcion varchar(20) NOT NULL,
	existencias float NOT NULL,
	precio_compra float NOT NULL,
	precio_venta float NOT NULL,
	imagen_producto varchar(30) NOT NULL
);

insert into productoss values ("1","Control","Xbox One","10","750","1000","xboxone.jpg");
insert into productoss values ("2","Bocina","Bose","5","2100","3000","bose.jpg");
insert into productoss values ("3","Bateria","Repuesto","100","65","120","pw.jpg");