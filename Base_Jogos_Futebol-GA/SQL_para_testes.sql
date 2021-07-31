SELECT * from GolsPorTime;
SELECT * FROM GolsPorCampeonatoAtleta;
SELECT * FROM GolsPorCampeonatoTime;
SELECT * FROM ItensPorJogador;


SELECT * FROM jogadores where CPF = "1";
SELECT * FROM clubes where id_clube = 1;
SELECT * FROM campeonatos where id_campeonato = 1;
SELECT * FROM desempenho where cpf = "1" AND id_partida = 1;
SELECT * FROM desempenho where cpf = "1" AND id_campeonato = 1;
SELECT * FROM desempenho where cpf = "1" AND id_clube = 1;
SELECT * FROM desempenho where cpf = "1" AND id_clube = 2;


INSERT INTO jogadores values ("Jogador ja existente", "1", 21);

INSERT INTO clubes values (1, "Clube ja existente");

