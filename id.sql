CREATE TABLE Menu(
Codigo_Menu bigInt Primary Key,
Nombre text Not Null,
UNIQUE(Nombre)
);

CREATE TABLE Perfil(
Codigo_Perfil bigInt Primary Key,
perfil text,
Codigo_menu bigint REFERENCES menu(Codigo_Menu),
);


CREATE TABLE OpcionesMenu(
Codigo_OpcionesMenu bigInt Primary Key,
OpcionesMenu text not null,
codigo_menu bigint REferences menu(Codigo_Menu) 
);

Create table estilos(
Codigo_estilo bigInt Primary key,
nombre text
);

CrEATE TABLE USUARIOS(
Codigo_Usuario BIGInt Primary Key,
Nombre Text Not NULL ,
Salt TEXT NOT NULL,
Contrase  TEXT NOT NULL,
Email text not null,
Fecha_registro_Error timestamp,
Contador_de_Inicios_Fallidos BigINt,
rol bigint  REFERENCES Perfil(Codigo_Perfil) not NULL,
Estilo bigInt References  estilos(Codigo_estilo) not NULL
);

INSERT INTO estilos(Codigo_estilo,nombre) values ('1','Cerulean');
INSERT INTO estilos(Codigo_estilo,nombre) values ('2','Cyborg');
INSERT INTO estilos(Codigo_estilo,nombre) values ('3','Darkly');
INSERT INTO estilos(Codigo_estilo,nombre) values ('4','Litera');

