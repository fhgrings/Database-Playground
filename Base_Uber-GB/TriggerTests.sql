Select * from InformacoesCondutor;

Select * from InformacoesCorrida;

Select * from InformacoesVeiculo;

-- CHECK PLACA = 7 caracteres
insert into Veiculo
values ("012345671238", "abc0f", 123);

-- INSERT Data final menor que data inicial
select * from Motorista; 
insert into Motorista (data_inicio, data_fim,renavan,CPF_condutor)
values ("2019-10-11 12:30:01", "2019-10-11 12:30:01", "012345681", "12345678901");

-- INSERT AVALICAO FORA DE 0 - 5
SELECT * FROM Corrida;
insert into Corrida (id_corrida,avaliacao_condutor
                     ,avaliacao_veiculo
                     ,data_inicio
                     ,data_fim
                     ,origem
                     ,destino
                     ,tarifa
                     ,distancia
                     ,id_motorista
                     ,CPF_passageiro)
values  (13,6,null,"2019-10-11 12:30:01", null , "sapiranga",       "sapiranga",          0.3, 0.5, 4, "01234567893");
--
insert into Corrida (id_corrida,avaliacao_condutor
                     ,avaliacao_veiculo
                     ,data_inicio
                     ,data_fim
                     ,origem
                     ,destino
                     ,tarifa
                     ,distancia
                     ,id_motorista
                     ,CPF_passageiro)
values  (13,-3,null,"2019-10-11 12:30:01", null , "sapiranga",       "sapiranga",          0.3, 0.5, 4, "01234567893");

-- TRIGGER Evita Mesmo veiculo em uso por dois motoristas
select * from Motorista; 
insert into Motorista (data_inicio, data_fim,renavan,CPF_condutor)
values (now(), now(), "012345682", "12345678901");


-- TRIGGER EvitaCondutorRetirar2Veiculos
select * from Motorista; 
insert into Motorista (data_inicio, data_fim,renavan,CPF_condutor)
values (now(), now(), "012345678", "12345678906");

-- TRIGGER EvitaPassageito2ViagensAoMesmoTempo
SELECT * FROM Corrida;
insert into Corrida (id_corrida,avaliacao_condutor
                     ,avaliacao_veiculo
                     ,data_inicio
                     ,data_fim
                     ,origem
                     ,destino
                     ,tarifa
                     ,distancia
                     ,id_motorista
                     ,CPF_passageiro)
values  (13,null,null,"2019-10-11 12:30:01", null , "sapiranga",       "sapiranga",          0.3, 0.5, 4, "01234567891");
        
-- TRIGGER EvitaCondutor2ViagensAoMesmoTempo
SELECT * FROM Corrida;
insert into Corrida (id_corrida,avaliacao_condutor
                     ,avaliacao_veiculo
                     ,data_inicio
                     ,data_fim
                     ,origem
                     ,destino
                     ,tarifa
                     ,distancia
                     ,id_motorista
                     ,CPF_passageiro)
values  (13,null,null,"2019-10-11 12:30:01", null , "sapiranga",       "sapiranga",          0.3, 0.5, 1, "01234567894");


