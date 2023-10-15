CREATE DATABASE db_web_crawler;
USE db_web_crawler;

CREATE TABLE registro(
	id_registro INT AUTO_INCREMENT,
    nome_utilizador VARCHAR(150),
    cpu_modelo VARCHAR(150),
    cpu_temp DECIMAL(4,1),
    cpu_uso DECIMAL(4,1),
    cpu_energia DECIMAL(3,1),
    ram_uso DECIMAL(4,1),
    ram_utilizada INT,
    ram_livro INT
)