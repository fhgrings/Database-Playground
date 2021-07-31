CREATE TABLE jogadores
(
    nome VARCHAR(40) NOT NULL,
    CPF VARCHAR(10),
    data_nascimento DATE,
    PRIMARY KEY (cpf)
);


CREATE TABLE campeonatos
(
    id_campeonato INT,
    PRIMARY KEY (id_campeonato),
    nome VARCHAR(40),
    data_inicio DATE,
    data_fim DATE
);
CREATE TABLE clubes
(
    id_clube INT,
    PRIMARY KEY (id_clube),
    nome VARCHAR(40)
);
CREATE TABLE partidas
(
    id_partida INT,
    PRIMARY KEY (id_partida),
    time_a INT,
    time_b INT,
    id_campeonato INT NOT NULL,
    CHECK (time_a != time_b),
    FOREIGN KEY (id_campeonato) REFERENCES campeonatos (id_campeonato),
    FOREIGN KEY (time_a) REFERENCES clubes (id_clube),
    FOREIGN KEY (time_b) REFERENCES clubes (id_clube) ON DELETE CASCADE
);
CREATE TABLE contrato
(
    id_contrato INT,
    PRIMARY KEY(id_contrato),
    CPF VARCHAR(40),
    id_clube INT,
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (id_clube) REFERENCES clubes (id_clube),
    FOREIGN KEY (CPF) REFERENCES jogadores (CPF)
);
CREATE TABLE desempenho
(
    id_desempenho INT,
    CPF VARCHAR(40),
    id_partida INT,
    PRIMARY KEY (id_desempenho, CPF, id_partida),
    RB INT,
    G INT,
    A INT,
    SG INT,
    FS INT,
    FF INT,
    FD INT,
    FT INT,
    DD INT,
    DP INT,
    GC INT,
    CV INT,
    CA INT,
    GS INT,
    PP INT,
    FC INT,
    I INT,
    PE INT,
    FOREIGN KEY (CPF) REFERENCES jogadores (CPF),
    FOREIGN KEY (id_partida) REFERENCES partidas (id_partida)
);

CREATE VIEW GolsPorTime
AS
    SELECT SUM(d.g) Gols, j.nome Jogador, c.nome Clube
    FROM desempenho d
        INNER JOIN jogadores j ON j.cpf = d.cpf
        INNER JOIN contrato jc ON jc.cpf = j.cpf
        INNER JOIN clubes c ON c.id_clube = jc.id_clube
        INNER JOIN partidas p ON p.id_partida = d.id_partida
        INNER JOIN campeonatos camp ON camp.id_campeonato = p.id_campeonato
    WHERE (jc.data_inicio < camp.data_inicio AND camp.data_inicio < jc.data_fim)
    OR (jc.data_inicio < camp.data_fim AND camp.data_fim < jc.data_fim) 
   GROUP BY
                Jogador, Clube
    HAVING 
                COUNT(*) > 0;

CREATE VIEW GolsPorCampeonatoAtleta
AS
    SELECT SUM(d.g) GOLS, c.nome Campeonato, j.nome Jogador, cl.nome
    FROM campeonatos c
        INNER JOIN partidas p ON p.id_campeonato = c.id_campeonato
        INNER JOIN desempenho d ON d.id_partida = p.id_partida
        INNER JOIN jogadores j ON j.cpf = d.cpf
        INNER JOIN contrato jc ON jc.cpf = j.cpf
        INNER JOIN clubes cl ON cl.id_clube = jc.id_clube
    WHERE (jc.data_inicio < c.data_inicio AND c.data_inicio < jc.data_fim)
    OR (jc.data_inicio < c.data_fim AND c.data_fim < jc.data_fim)
    GROUP BY 
 j.nome, c.nome, c.id_campeonato, cl.nome
    having 
 count(*) > 0;



CREATE VIEW GolsPorCampeonatoTime
AS
    SELECT SUM(d.g) Gols_feitos, SUM(d.gs) Gols_sofridos, (SUM(d.g) - SUM(d.gs)) Saldo_de_gols, c.nome Campeonato, j.nome Jogador, cb.nome Clube
    FROM campeonatos c
        INNER JOIN partidas p ON p.id_campeonato = c.id_campeonato
        INNER JOIN desempenho d ON d.id_partida = p.id_partida
        INNER JOIN jogadores j ON j.cpf = d.cpf
        INNER JOIN contrato jc ON jc.cpf = j.cpf
        INNER JOIN clubes cb ON cb.id_clube = jc.id_clube
    WHERE (jc.data_inicio < c.data_inicio AND c.data_inicio < jc.data_fim)
    OR (jc.data_inicio < c.data_fim AND c.data_fim < jc.data_fim)  
  GROUP BY 
 j.nome, c.nome, cb.nome
    HAVING 
 count(*) > 0;


CREATE VIEW ItensPorJogador
AS
    SELECT c.nome Campeonato, j.nome Jogador, cb.nome Clube, SUM(d.rb) Roubadas_de_Bola, SUM(d.g) Gols, SUM(d.a) Assistencia, SUM(d.sg) Jogos_sem_sofrer_gols, SUM(d.fs) Falta_Sofrida, SUM(d.ff) Finalização_fora, SUM(d.fd) finalização_defendida, SUM(d.ft) Finalização_trave, SUM(d.dd) Defesa_dificil, SUM(d.dp) Defesa_Penalti, SUM(d.gc) Gol_Contra, SUM(d.cv) Cartão_Vermelho, SUM(d.ca) Cartão_Amarelo, SUM(d.gs) Gol_Sofrido, SUM(d.pp) Penalti_perdido, SUM(d.fc) Falta_Cometida, SUM(d.i) Impedimento, SUM(d.pe) Passes_Errados
    FROM campeonatos c
        INNER JOIN partidas p ON p.id_campeonato = c.id_campeonato
        INNER JOIN desempenho d ON d.id_partida = p.id_partida
        INNER JOIN jogadores j ON j.cpf = d.cpf
        INNER JOIN contrato jc ON jc.cpf = j.cpf
        INNER JOIN clubes cb ON cb.id_clube = jc.id_clube
    GROUP BY 
 j.nome, c.nome, cb.nome
    HAVING 
 count(*) >1;


INSERT INTO jogadores
values
    ("Felipe Grings", "1", '1998-01-01');
INSERT INTO jogadores
values
    ("Jonas", "2", '1995-01-01');
INSERT INTO jogadores
values
    ("João", "3", '1993-01-01');
INSERT INTO jogadores
values
    ("Armando", "4", '1992-01-01');
INSERT INTO jogadores
values
    ("Elvis", "5", '1994-01-01');

INSERT INTO clubes
values
    (1, "Gremio");
INSERT INTO clubes
values
    (2, "Inter");
INSERT INTO clubes
values
    (3, "Flamengo");
INSERT INTO clubes
values
    (4, "Sao Paulo");
INSERT INTO clubes
values
    (5, "Vitoria");

INSERT INTO contrato
VALUES
    (1, "1", 1, '2012-01-01', '2012-12-12');
INSERT INTO contrato
VALUES
    (2, "1", 2, '2013-01-01', '2015-12-12');
INSERT INTO contrato
VALUES
    (3, "2", 2, '2012-01-01', '2015-12-03');
INSERT INTO contrato
VALUES
    (4, "3", 3, '2012-01-01', '2015-12-03');
INSERT INTO contrato
VALUES
    (5, "4", 4, '2012-01-01', '2015-12-03');
INSERT INTO contrato
VALUES
    (6, "5", 5, '2012-01-01', '2012-12-03');
INSERT INTO contrato
VALUES
    (7, "5", 1, '2013-01-01', '2015-12-12');

INSERT INTO campeonatos
VALUES
    (1, "Brasileirão 2012", '2012-02-02', '2012-12-01');
INSERT INTO campeonatos
VALUES
    (2, "Gauchão 2012", '2012-01-01', '2012-12-01');
INSERT INTO campeonatos
VALUES
    (3, "Brasileirão 2013", '2013-01-01', '2013-12-01');
INSERT INTO campeonatos
VALUES
    (4, "Gauchão 2013", '2013-01-01', '2013-12-01');

INSERT INTO partidas
VALUES
    (1, 1, 2, 1);
INSERT INTO partidas
VALUES
    (2, 1, 3, 1);
INSERT INTO partidas
VALUES
    (3, 1, 4, 1);
INSERT INTO partidas
VALUES
    (4, 1, 5, 1);
INSERT INTO partidas
VALUES
    (5, 2, 1, 1);
INSERT INTO partidas
VALUES
    (6, 2, 3, 1);
INSERT INTO partidas
VALUES
    (7, 2, 4, 1);
INSERT INTO partidas
VALUES
    (8, 2, 5, 1);

INSERT INTO partidas
VALUES
    (9, 1, 2, 2);
INSERT INTO partidas
VALUES
    (10, 1, 3, 2);
INSERT INTO partidas
VALUES
    (11, 1, 4, 2);
INSERT INTO partidas
VALUES
    (12, 1, 5, 2);
INSERT INTO partidas
VALUES
    (13, 2, 1, 2);
INSERT INTO partidas
VALUES
    (14, 2, 3, 2);
INSERT INTO partidas
VALUES
    (15, 2, 4, 2);
INSERT INTO partidas
VALUES
    (16, 2, 5, 2);

INSERT INTO partidas
VALUES
    (17, 1, 2, 3);
INSERT INTO partidas
VALUES
    (18, 1, 3, 3);
INSERT INTO partidas
VALUES
    (19, 1, 4, 3);
INSERT INTO partidas
VALUES
    (20, 1, 5, 3);

INSERT INTO desempenho
VALUES(1, 1, 1, 12, 1, 3, 4, 4, 7, 3, 3, 1, 2, 1, 1, 3, 2, 2, 2, 1, 8);
INSERT INTO desempenho
VALUES(2, 1, 2, 15, 1, 4, 1, 8, 10, 8, 4, 3, 1, 1, 4, 2, 2, 2, 3, 2, 17);
INSERT INTO desempenho
VALUES(3, 1, 3, 5, 0, 4, 5, 4, 9, 1, 4, 3, 4, 1, 2, 4, 1, 2, 4, 2, 14);
INSERT INTO desempenho
VALUES(4, 1, 4, 20, 2, 3, 5, 4, 1, 9, 3, 4, 4, 1, 2, 1, 4, 1, 6, 2, 2);
INSERT INTO desempenho
VALUES(5, 2, 1, 14, 1, 2, 1, 5, 6, 3, 3, 3, 2, 1, 4, 4, 1, 2, 4, 1, 6);
INSERT INTO desempenho
VALUES(6, 2, 6, 16, 3, 1, 3, 4, 5, 10, 2, 2, 5, 1, 3, 2, 2, 2, 2, 2, 2);
INSERT INTO desempenho
VALUES(7, 1, 5, 7, 0, 1, 3, 4, 10, 5, 5, 3, 1, 1, 4, 1, 2, 1, 4, 2, 6);
INSERT INTO desempenho
VALUES(8, 2, 8, 8, 1, 2, 2, 6, 1, 1, 1, 4, 2, 1, 2, 2, 5, 2, 3, 1, 15);
INSERT INTO desempenho
VALUES(9, 3, 2, 2, 0, 1, 4, 3, 8, 1, 2, 3, 3, 1, 3, 4, 3, 1, 6, 2, 2);
INSERT INTO desempenho
VALUES(10, 4, 3, 12, 1, 2, 2, 4, 2, 1, 3, 1, 2, 1, 1, 4, 1, 2, 4, 2, 15);
INSERT INTO desempenho
VALUES(11, 5, 4, 7, 1, 4, 5, 1, 1, 8, 5, 1, 2, 1, 3, 4, 5, 2, 6, 2, 20);
INSERT INTO desempenho
VALUES(12, 3, 6, 20, 0, 3, 5, 4, 6, 4, 1, 4, 2, 1, 1, 4, 3, 1, 2, 2, 19);
INSERT INTO desempenho
VALUES(13, 4, 7, 15, 3, 3, 3, 7, 3, 7, 5, 5, 3, 1, 1, 4, 2, 2, 6, 2, 20);
INSERT INTO desempenho
VALUES(14, 5, 8, 12, 4, 4, 3, 1, 8, 6, 5, 4, 2, 1, 1, 1, 3, 2, 2, 1, 11);
INSERT INTO desempenho
VALUES(15, 1, 7, 15, 2, 1, 1, 7, 4, 2, 3, 4, 3, 1, 2, 2, 1, 2, 6, 1, 15);
INSERT INTO desempenho
VALUES(16, 2, 1, 19, 0, 1, 3, 2, 9, 5, 1, 5, 5, 1, 1, 2, 1, 1, 6, 2, 7);
INSERT INTO desempenho
VALUES(17, 5, 17, 19, 0, 1, 3, 2, 9, 5, 1, 5, 5, 1, 1, 2, 1, 1, 6, 2, 7);
INSERT INTO desempenho
VALUES(18, 1, 17, 19, 2, 1, 3, 2, 9, 5, 1, 5, 5, 1, 1, 2, 1, 1, 6, 2, 7);