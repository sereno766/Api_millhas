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
('Ana Clara Souza', 'ana.souza@email.com', '1234-5678-9012-3456', 35000, 'Paris'),
('Bruno Henrique Lima', 'bruno.lima@email.com', '2345-6789-0123-4567', 12000, 'Rio de Janeiro'),
('Carla Menezes', 'carla.menezes@email.com', '3456-7890-1234-5678', 80000, 'Nova York'),
('Daniel Ferreira', 'daniel.ferreira@email.com', '4567-8901-2345-6789', 5000, 'Gramado'),
('Eduarda Martins', 'eduarda.martins@email.com', '5678-9012-3456-7890', 25000, 'Lisboa'),
('Felipe Alves', 'felipe.alves@email.com', '6789-0123-4567-8901', 47000, 'Orlando'),
('Gabriela Rocha', 'gabriela.rocha@email.com', '7890-1234-5678-9012', 15000, 'Buenos Aires'),
('Henrique Costa', 'henrique.costa@email.com', '8901-2345-6789-0123', 95000, 'Tóquio'),
('Isabela Nunes', 'isabela.nunes@email.com', '9012-3456-7890-1234', 22000, 'Toronto'),
('João Pedro Silva', 'joao.silva@email.com', '0123-4567-8901-2345', 3000, 'Florianópolis'),
('Karen Moreira', 'karen.moreira@email.com', '1357-2468-3579-4680', 41000, 'Roma'),
('Leonardo Pires', 'leonardo.pires@email.com', '2468-3579-4680-5791', 28000, 'Londres'),
('Mariana Ribeiro', 'mariana.ribeiro@email.com', '3579-4680-5791-6802', 67000, 'Cancún'),
('Nicolas Duarte', 'nicolas.duarte@email.com', '4680-5791-6802-7913', 11000, 'Fortaleza'),
('Otávio Gomes', 'otavio.gomes@email.com', '5791-6802-7913-8024', 52000, 'Madrid'),
('Paula Carvalho', 'paula.carvalho@email.com', '6802-7913-8024-9135', 86000, 'Dubai'),
('Rafael Santos', 'rafael.santos@email.com', '7913-8024-9135-0246', 17500, 'Santiago'),
('Sofia Teixeira', 'sofia.teixeira@email.com', '8024-9135-0246-1357', 9000, 'Curitiba'),
('Thiago Barros', 'thiago.barros@email.com', '9135-0246-1357-2468', 30000, 'Berlim'),
('Vitória Almeida', 'vitoria.almeida@email.com', '0246-1357-2468-3579', 48000, 'Atenas');


SELECT * FROM cliente;