DROP DATABASE IF EXISTS db_web_crawler;

CREATE DATABASE db_web_crawler;
USE db_web_crawler;

CREATE USER IF NOT EXISTS userCrawler IDENTIFIED BY 'urubu100';

CREATE TABLE tb_registro(
	id_registro INT PRIMARY KEY AUTO_INCREMENT,
    nome_pc VARCHAR(150),
    cpu_modelo VARCHAR(150),
    cpu_temp DECIMAL(4,1),
    cpu_uso DECIMAL(4,1),
    cpu_energia DECIMAL(3,1),
    ram_uso DECIMAL(4,1),
    ram_utilizada INT,
    ram_livre INT
);

GRANT INSERT ON db_web_crawler.tb_registro TO userCrawler;
FLUSH PRIVILEGES;

SELECT * FROM tb_registro ORDER BY id_registro desc;