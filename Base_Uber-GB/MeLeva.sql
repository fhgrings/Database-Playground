drop table if exists Corrida;
drop table if exists Motorista;
drop table if exists Condutor;
drop table if exists Veiculo;
drop table if exists ModeloVeiculo;
drop table if exists Passageiro;
drop view if exists InformacoesCorrida;
drop view if exists InformacoesVeiculo;
drop view if exists InformacoesCondutor;


CREATE TABLE Condutor (
    CPF_condutor varchar(11) PRIMARY KEY,
    Nome varchar (20) NOT NULL,
    Telefone varchar(20) NOT NULL,
    Data_cadastro TIMESTAMP NOT NULL
);

CREATE TABLE ModeloVeiculo (
	id_modelo_Veiculo int PRIMARY KEY auto_increment,
    modelo varchar(20) NOT NULL,
    marca VARCHAR(20) NOT NULL,
    ano VARCHAR(4) NOT NULL
);

CREATE TABLE Veiculo (
    renavan varchar(20) PRIMARY KEY,
    placa VARCHAR(7) CONSTRAINT quantidade_caracteres_placa CHECK (CHAR_LENGTH (placa) = 7),
    id_modelo_veiculo int,
    FOREIGN KEY (id_modelo_veiculo) REFERENCES ModeloVeiculo (id_modelo_veiculo)
);

CREATE TABLE Motorista (
    id_motorista int PRIMARY KEY AUTO_INCREMENT,
    CPF_condutor VARCHAR(11) NOT NULL,
    renavan VARCHAR(20) NOT NULL,
    data_inicio TIMESTAMP NOT NULL,
    data_fim TIMESTAMP,
    CONSTRAINT motorista_data_final_menor_data_inicial CHECK (timestampdiff(SECOND,data_inicio, data_fim) >= 0),
    UNIQUE(CPF_condutor, renavan, data_inicio),
    FOREIGN KEY (CPF_condutor) REFERENCES Condutor (CPF_condutor),
    FOREIGN KEY (renavan) REFERENCES Veiculo (renavan)
);

CREATE TABLE Passageiro (
    CPF_passageiro VARCHAR(11) PRIMARY KEY,
    nome varchar(20) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    data_cadastro TIMESTAMP NOT NULL
);

CREATE TABLE Corrida (
    id_corrida int,
    id_motorista int,
    CPF_passageiro VARCHAR(11),
    avaliacao_condutor int CONSTRAINT avaliacao_condutor_fora_do_range CHECK (avaliacao_condutor >= 0 AND avaliacao_condutor <= 5),
    avaliacao_veiculo int CONSTRAINT avaliacao_veiculo_fora_do_range CHECK (avaliacao_veiculo >= 0 AND avaliacao_veiculo <= 5),
    data_inicio TIMESTAMP NOT NULL,
    data_fim TIMESTAMP,
    CONSTRAINT corrida_data_final_menor_data_inicial CHECK (timestampdiff(SECOND,data_inicio, data_fim) >= 0),
    origem varchar(20) NOT NULL,
    destino varchar(20) NOT NULL,
    tarifa float NOT NULL,
    distancia float NOT NULL,

    PRIMARY KEY (id_motorista, CPF_passageiro, id_corrida),
    FOREIGN KEY (id_motorista) REFERENCES Motorista (id_motorista),
    FOREIGN KEY (CPF_passageiro) REFERENCES Passageiro (CPF_passageiro)
);

delimiter $$
create trigger EvitaPassageiro2ViagensAoMesmoTempo BEFORE INSERT ON Corrida
FOR EACH ROW 
BEGIN
	if ( (SELECT COUNT(*) FROM Corrida C WHERE C.CPF_passageiro = new.CPF_passageiro AND C.data_inicio IS NOT NULL AND C.data_fim IS NULL) <> 0) THEN
		SIGNAL SQLSTATE '45000' SET message_text = 'Passageiro em corrida';		
    END IF;
END $$
delimiter ;


delimiter $$
create trigger EvitaCondutor2ViagensAoMesmoTempo BEFORE INSERT ON Corrida
FOR EACH ROW 
BEGIN
	if ( (SELECT COUNT(*) FROM Corrida C WHERE C.id_motorista = new.id_motorista AND C.data_inicio IS NOT NULL AND C.data_fim IS NULL) <> 0) THEN
		SIGNAL SQLSTATE '45000' SET message_text = 'Condutor em corrida';		
    END IF;
END $$
delimiter ;

delimiter $$
create trigger EvitaVeiculoRetiradoAoMesmoTempo BEFORE INSERT ON Motorista
FOR EACH ROW 
BEGIN
	if ( (SELECT COUNT(*) FROM Motorista M WHERE M.renavan = new.renavan AND M.data_inicio IS NOT NULL AND M.data_fim IS NULL) <> 0) THEN
		SIGNAL SQLSTATE '45000' SET message_text = 'Veiculo em uso';		
    END IF;
END $$
delimiter ;

delimiter $$
create trigger EvitaCondutorRetirar2Veiculos BEFORE INSERT ON Motorista
FOR EACH ROW 
BEGIN
	if ( (SELECT COUNT(*) FROM Motorista M WHERE M.CPF_condutor = new.CPF_condutor AND M.data_inicio IS NOT NULL AND M.data_fim IS NULL) <> 0) THEN
		SIGNAL SQLSTATE '45000' SET message_text = 'Motorista Ja está com um veículo';		
    END IF;
END $$
delimiter ;


CREATE VIEW InformacoesCorrida
AS
		SELECT CN.CPF_condutor, CN.Nome Condutor_nome, P.CPF_passageiro, P.nome Passageiro_nome, C.origem, C.destino, C.distancia,
        ROUND(((5 + C.distancia * 0.8 + (timestampdiff(SECOND,C.data_inicio, C.data_fim) / 60) * 0.2)*C.tarifa), 2) Valor,
		C.data_inicio, ROUND(timestampdiff(SECOND,C.data_inicio, C.data_fim) / 60, 2) Duracao, 
        V.*, MV.marca, MV.ano,
        C.avaliacao_condutor, C.avaliacao_veiculo
      FROM Corrida C 
        INNER JOIN Passageiro P ON P.CPF_passageiro = C.CPF_passageiro
        INNER JOIN Motorista M ON M.id_motorista = C.id_motorista
        INNER JOIN Veiculo V ON V.renavan = M.renavan
        INNER JOIN ModeloVeiculo MV ON MV.id_modelo_veiculo = V.id_modelo_veiculo
        INNER JOIN Condutor CN ON CN.CPF_condutor = M.CPF_condutor;


CREATE VIEW InformacoesCondutor
AS
		SELECT CN.CPF_condutor, CN.nome, COUNT(C.avaliacao_condutor) QuantidadeAvalicoes,
			ROUND(AVG(C.avaliacao_condutor),2) Media_avaliacoes,
            COUNT(CN.CPF_condutor) Quantidade_Corridas,
            ROUND(SUM(((5 + C.distancia * 0.8 + (timestampdiff(SECOND,C.data_inicio, C.data_fim) / 60)*C.tarifa))) * 0.1, 2) Pagamento
    FROM Corrida C
        INNER JOIN Motorista M ON M.id_motorista = C.id_motorista
        INNER JOIN Condutor CN ON CN.CPF_condutor = M.CPF_condutor
	GROUP BY CN.CPF_Condutor; 
        

CREATE VIEW InformacoesVeiculo
AS  
    SELECT V.placa, V.renavan, MV.modelo, MV.marca, MV.ano, COUNT(V.renavan) QuantidadeCorridas, COUNT(C.avaliacao_veiculo) QuantidadeAvalicoes, 
    ROUND(AVG(C.avaliacao_veiculo), 2) Med_Avaliacao_Veiculo
    FROM Corrida C
        INNER JOIN Motorista M ON M.id_motorista = C.id_motorista
        INNER JOIN Veiculo V ON V.renavan = M.renavan
        INNER JOIN ModeloVeiculo MV ON MV.id_modelo_veiculo = V.id_modelo_veiculo
	GROUP BY M.renavan;



insert into Condutor
values ("12345678901", "Martin Scorcese", "123456789", now()),
       ("12345678902", "Falcão",          "999999991", now()),
       ("12345678903", "Jorge",           "999999992", now()),
       ("12345678904", "Niki Lauda",      "999999993", now()),
       ("12345678905", "James Hunt",      "999999994", now()),
       ("12345678906", "Frank Martin",    "999999995", now()),
       ("12345678908", "Nathanne",        "999999998", now());


insert into ModeloVeiculo (modelo, marca, ano)
values ("G650GS", "BMW", "2012"),
       ("Mirage 250", "Hyosung", "2012"),
       ("Street Bob", "Harley Davidson", "2012"),
       ("Scrambler", "Ducati", "2012");

insert into Veiculo
values ("012345678", "abc0f12", 1),
       ("012345679", "abc0f13", 2),
       ("012345680", "abc0f14", 3),
       ("012345681", "abc0f15", 1),
       ("012345682", "abc0f16", 1),
       ("012345683", "abc0f17", 1),
       ("012345684", "abc0f18", 1),
       ("012345685", "abc0f19", 1),
       ("012345686", "abc0f20", 1),
       ("012345687", "abc0f21", 1),
       ("012345688", "abc0f22", 1),
       ("012345689", "abc0023", 2),
       ("012345690", "abc0024", 2),
       ("012345691", "abd0025", 2),
       ("012345692", "abe0026", 2),
       ("012345693", "abe0146", 3),
       ("012345694", "abe0147", 4),
       ("012345695", "abe0148", 4);

insert into Motorista (data_inicio, data_fim,renavan,CPF_condutor)
values (now(), now(), "012345678", "12345678901"),
       (now(), now(), "012345679", "12345678902"),
       (now(), now(), "012345680", "12345678903"),
       (now(), now(), "012345681", "12345678904"),
       (now(), now(), "012345682", "12345678905"),
       (now(), null,  "012345682", "12345678906");

insert into Passageiro (nome, telefone, data_cadastro, CPF_passageiro)
values  ("Kobayashi",    "012345678", now(), "01234567890"),
        ("Kanna",        "012345679", now(), "01234567891"),
        ("Arthur Fleck", "012345680", now(), "01234567892"),
        ("Tooruh",       "012345681", now(), "01234567893"),
        ("Senku",        "012345682", now(), "01234567894");

insert into Corrida (id_corrida
					 ,avaliacao_condutor
                     ,avaliacao_veiculo
                     ,data_inicio
                     ,data_fim
                     ,origem
                     ,destino
                     ,tarifa
                     ,distancia
                     ,id_motorista
                     ,CPF_passageiro)
values  (1,5,5,      "2019-10-11 12:30:01", "2019-10-11 12:41:31", "sapiranga",       "sapiranga",          0.3, 0.5, 1, "01234567890"),
        (2,1,4,      "2019-10-12 12:30:01", "2019-10-12 12:41:31", "novo hamburgo",   "novo hamburgo",      0.6, 0.7, 2, "01234567891"),
        (3,3,2,      "2019-10-13 12:30:01", "2019-10-13 12:41:31", "são leopoldo",    "novo hamburgo",      0.8, 0.8, 3, "01234567892"),
        (4,4,1,      "2019-10-14 12:30:01", "2019-10-14 12:41:31", "campo bom",       "campo bom",          0.9, 0.9, 4, "01234567893"),
        (5,2,0,      "2019-10-15 12:30:01", "2019-10-15 12:41:31", "porto alegre",    "porto alegre",       0.6, 0.1, 5, "01234567894"),
        (6,2,4,      "2019-10-16 12:30:01", "2019-10-16 12:41:31", "canoas",          "canoas",             0.1, 0.3, 1, "01234567891"),
        (7,3,4,      "2019-10-17 12:30:01", "2019-10-17 12:41:31", "esteio",          "canoas",             0.2, 0.4, 2, "01234567891"),
        (8,4,5,      "2019-10-18 12:30:01", "2019-10-18 12:41:31", "sapucaia do sul", "são leopoldo",       0.3, 0.5, 3, "01234567891"),
        (9,1,4,      "2019-10-19 12:30:01", "2019-10-19 12:41:31", "sapiranga",       "sapiranga",          0.5, 0.6, 4, "01234567892"),
        (10,1,4,      "2019-10-20 12:30:01", "2019-10-20 12:41:31", "sapiranga",       "sapiranga",          0.7, 1.7, 5, "01234567892"),
        (11,4,null,"2019-10-20 12:30:01",  null,                 "sapiranga",       "sapiranga",          0.7, 1.7, 5, "01234567892"),
        (12,3,null,"2019-10-20 12:30:01",  null,                 "sapiranga",       "sapiranga",          0.7, 1.7, 1, "01234567891");


