create database db_filmes

use db_filmes 

-- drop database db_filmes_test
-- drop database db_filmes

/*----------Criando Tabelas----------*/
create table tb_genero
(
cd_genero int not null primary key identity(1, 1),
genero varchar(50) not null
)

create table tb_filme
(
cd_filme int not null primary key,
filme varchar(100) not null,
tempo_min int not null,
cd_genero int foreign key 
references tb_genero(cd_genero)
)
--drop table tb_filme
--drop table tb_genero
/*-----------------------------------*/



-- Populando ---------------
insert into tb_genero
(genero)
values
('Ficção científica'),
('Drama'),
('Ação'),
('Suspense'),
('Romance'),
('Terror'),
('Aventura'),
('Cinema de arte'),
('Comédia'),
('Comédia de ação'),
('Comédia de terror'),
('Comédia dramática'),
('Comédia romântica'),
('Dança'),
('Documentário'),
('Docuficção'),
('Espionagem'),
('Faroeste'),
('Fantasia'),
('Fantasia científica'),
('Ficção científica'),
('Filmes com truques'),
('Filmes de guerra'),
('Mistério'),
('Musical'),
('Filme policial')

insert into tb_filme
(cd_filme, filme, tempo_min, cd_genero)
values
(7, 'O retorno da sua mãe', 666, 6),
(1, 'Interestelar', 180, 1),
(2, 'Pulp Fiction', 140, 2),
(3, 'The Batman', 180, 3),
(4, 'Clube da Luta', 130, 4),
(5, 'A Culpa é das Estrelas', 130, 5)
-- -------------------------


select * from tb_genero
select * from tb_filme
-- delete from tb_filme where cd_filme = ?


/*------------VIEW-----------*/
-- Select
create view tb_filme_all as
select cd_filme, filme, tempo_min, G.genero 
from tb_filme F inner join tb_genero G
on F.cd_genero = G.cd_genero

select * from tb_filme_all
/*---------------------------*/

/*-----STORED PROCEDURES-----*/
-- Insert
CREATE PROCEDURE insert_filme @cd int, @filme varchar(100), @tempo int, @genero int
as
insert into tb_filme
(cd_filme, filme, tempo_min, cd_genero)
values
(@cd, @filme, @tempo, @genero)
GO

CREATE PROCEDURE insert_genero @genero varchar(50)
as
insert into tb_genero
(genero)
values
(@genero)
GO

-- exec insert_filme @cd = 10, @filme = 'A chegada da sua mãe', @tempo = 120, @genero = 6
-- exec insert_genero @genero = 'Aventura'

-- Update
CREATE PROCEDURE update_filme_nome @cd int, @filme varchar(100)
as
update tb_filme
	set filme = @filme
	where cd_filme = @cd
GO

CREATE PROCEDURE update_filme_tempo @cd int, @tempo int
as
update tb_filme
	set tempo_min = @tempo
	where cd_filme = @cd
GO

CREATE PROCEDURE update_filme_genero @cd int, @genero int
as
update tb_filme
	set cd_genero = @genero
	where cd_filme = @cd
GO

-- exec update_filme_nome @cd = 3, @filme = 'The Batman 2'
-- exec update_filme_tempo @cd = 3, @tempo = 190
-- exec update_filme_genero @cd = 3, @genero = 7


-- Delete
CREATE PROCEDURE delete_filme @cd int
as
delete from tb_filme where cd_filme = @cd
GO

exec delete_filme 10
/*---------------------------*/



