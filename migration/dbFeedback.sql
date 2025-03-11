create database dbFeedback;
use dbFeedback;

create table tb_comentarios(

	nome varchar (150) not null,
    data_hora datetime not null,
    comentario text not null,
    cod_comentario int auto_increment primary key

);

select * from tb_comentarios;