create database escola;

use escola;

create table aluno(
    id int not null primary key,
    nome varchar(50) not null,
    email varchar(50) not null,
    endereco varchar(50) not null
)

insert into aluno(id, nome, email, endereco) values (1, 'Lucas', 'lucas@hotmail.com', 'Rua Floriano')

SELECT*from aluno