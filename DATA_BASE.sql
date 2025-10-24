DROP DATABASE IF EXISTS DBMILHAS;
CREATE DATABASE DBMILHAS;
USE DBMILHAS;
SET SQL_SAFE_UPDATES=0;

CREATE TABLE cliente(
ID_cliente INT auto_increment NOT NULL
, NOME VARCHAR(100) 
, EMAIL VARCHAR(100) 
, CARTAO VARCHAR(20)
, SALDO_MILHAS INT 
, DESTINO_DESEJADO VARCHAR(100) 
, PRIMARY KEY (ID_cliente)
);


-- POPULAR A TABELA 
INSERT INTO cliente (NOME, EMAIL, CARTAO, SALDO_MILHAS, DESTINO_DESEJADO) VALUES
('Ana Clara Souza', 'ana.souza@email.com', 'Gold', 35000, 'Paris'),
('Bruno Henrique Lima', 'bruno.lima@email.com', 'Silver', 12000, 'Rio de Janeiro'),
('Carla Menezes', 'carla.menezes@email.com', 'Black', 80000, 'Nova York'),
('Daniel Ferreira', 'daniel.ferreira@email.com', 'Gold', 5000, 'Gramado'),
('Eduarda Martins', 'eduarda.martins@email.com', 'Platinum', 25000, 'Lisboa'),
('Felipe Alves', 'felipe.alves@email.com', 'Gold', 47000, 'Orlando'),
('Gabriela Rocha', 'gabriela.rocha@email.com', 'Silver', 15000, 'Buenos Aires'),
('Henrique Costa', 'henrique.costa@email.com', 'Black', 95000, 'Tóquio'),
('Isabela Nunes', 'isabela.nunes@email.com', 'Gold', 22000, 'Toronto'),
('João Pedro Silva', 'joao.silva@email.com', 'Silver', 3000, 'Florianópolis'),
('Karen Moreira', 'karen.moreira@email.com', 'Platinum', 41000, 'Roma'),
('Leonardo Pires', 'leonardo.pires@email.com', 'Gold', 28000, 'Londres'),
('Mariana Ribeiro', 'mariana.ribeiro@email.com', 'Black', 67000, 'Cancún'),
('Nicolas Duarte', 'nicolas.duarte@email.com', 'Silver', 11000, 'Fortaleza'),
('Otávio Gomes', 'otavio.gomes@email.com', 'Platinum', 52000, 'Madrid'),
('Paula Carvalho', 'paula.carvalho@email.com', 'Black', 86000, 'Dubai'),
('Rafael Santos', 'rafael.santos@email.com', 'Gold', 17500, 'Santiago'),
('Sofia Teixeira', 'sofia.teixeira@email.com', 'Silver', 9000, 'Curitiba'),
('Thiago Barros', 'thiago.barros@email.com', 'Platinum', 30000, 'Berlim'),
('Vitória Almeida', 'vitoria.almeida@email.com', 'Infinite', 48000, 'Atenas');


SELECT * FROM cliente;