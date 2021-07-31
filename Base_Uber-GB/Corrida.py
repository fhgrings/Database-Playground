# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:03:23 2019

@author: Cristian
"""
    
import CRUD as CRUD

#%%

class Corrida(CRUD):
    
    banco = None
    cursor = None
    tabela = "Corrida"

    def __init__(self,dados=None):
        Corrida.banco = super().banco
        Corrida.cursor = super().cursor
        if dados == None:
            self.__id_motorista          = None
            self.__CPF_passageiro        = None
            self.__id_corrida            = None
            self.__avaliacao_condutor    = None
            self.__avaliacao_veiculo     = None
            self.__data_inicio           = None
            self.__data_fim              = None
            self.__origem                = None
            self.__destino               = None
            self.__tarifa                = None
            self.__distancia             = None
        else:   
            self.fromTuple(dados)
    
    @property
    def id_motorista(self):
        return self.__id_motorista
    
    @property
    def CPF_passageiro(self):
        return self.__CPF_passageiro
    
    @CPF_passageiro.setter
    def CPF_passageiro(self,CPF_passageiro):
        self.__CPF_passageiro = CPF_passageiro
        self.atualizar()

    @property
    def id_corrida(self):
        return self.__id_corrida
    
    @id_corrida.setter
    def id_corrida(self,id_corrida):
        self.__id_corrida = id_corrida
        self.atualizar()
        
    @property
    def avaliacao_condutor(self):
        return self.__avaliacao_condutor
    
    @avaliacao_condutor.setter
    def avaliacao_condutor(self,avaliacao_condutor):
        self.__avaliacao_condutor = avaliacao_condutor
        self.atualizar()
    
    @property
    def avaliacao_veiculo(self):
        return self.__avaliacao_veiculo
    
    @avaliacao_veiculo.setter
    def avaliacao_veiculo(self,avaliacao_veiculo):
        self.__avaliacao_veiculo = avaliacao_veiculo
        self.atualizar()

    @property
    def data_inicio(self):
        return self.__data_inicio
    
    @data_inicio.setter
    def data_inicio(self,data_inicio):
        self.__data_inicio = data_inicio
        self.atualizar()
        
    @property
    def data_fim(self):
        return self.__data_fim
    
    @data_fim.setter
    def data_fim(self,data_fim):
        self.__data_fim = data_fim
        self.atualizar()
  
    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self,origem):
        self.__origem = origem
        self.atualizar()
    
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self,destino):
        self.__destino = destino
        self.atualizar()

    @property
    def tarifa(self):
        return self.__tarifa
    
    @tarifa.setter
    def tarifa(self,tarifa):
        self.__tarifa = tarifa
        self.atualizar()
        
    @property
    def distancia(self):
        return self.__distancia
    
    @distancia.setter
    def distancia(self,distancia):
        self.__distancia = distancia
        self.atualizar()        
        
    def novo(self, id_motorista=None,CPF_passageiro=None,id_corrida=None,avaliacao_condutor=None,avaliacao_veiculo=None,data_inicio=None,data_fim=None,origem=None,destino=None,tarifa=None,distancia=None):
        self.cursor.execute(f"INSERT INTO {self.tabela} (id_motorista,CPF_passageiro,id_corrida,avaliacao_condutor,avaliacao_veiculo,data_inicio,data_fim,origem,destino,tarifa,distancia) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_motorista,CPF_passageiro,id_corrida,avaliacao_condutor,avaliacao_veiculo,data_inicio,data_fim,origem,destino,tarifa,distancia))
        self.banco.commit()
        self.id_motorista = self.cursor.lastrowid
        
    def ler(self,id=None):
        if id:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE id_motorista=%s",(id,))    
        elif self.__id_corrida != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE id_motorista=%s",(self.__id_motorista,))
        else:
            raise Exception("Necessário passar o id_motorista")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)

    def atualizar(self):
        if self.__id_motorista:
            self.cursor.execute(f"UPDATE {self.tabela} SET CPF_passageiro=%s,id_corrida=%s,avaliacao_condutor=%s,avaliacao_veiculo=%s,data_inicio=%s,data_fim=%s,origem=%s,destino=%s,tarifa=%s,distancia=%s WHERE id_motorista=%s",(self.__CPF_passageiro,self.__id_corrida,self.__avaliacao_condutor,self.__avaliacao_veiculo,self.__data_inicio,self.__data_fim,self.__origem,self.__destino,self.__tarifa,self.__distancia,self.__id_motorista))
            self.banco.commit()
            return self.cursor.rowcount
        else:
            raise Exception("É necessário possuir um id_motorista para atualizar")
    
    def apagar(self):
        if self.__id_motorista:
            pass # SQL apagar e zerar o id
        else:
            raise Exception("Necessário id_motorista para remover")
    
    def fromTuple(self,dados):
        if len(dados) == 11:
            self.__id_motorista          = dados[0]
            self.__CPF_passageiro        = dados[1]
            self.__id_corrida            = dados[2]
            self.__avaliacao_condutor    = dados[3]
            self.__avaliacao_veiculo     = dados[4]
            self.__data_inicio           = dados[5]
            self.__data_fim              = dados[6]
            self.__origem                = dados[7]
            self.__destino               = dados[8]
            self.__tarifa                = dados[9]
            self.__distancia             = dados[10]

    def toTuple(self):
        if self.__id_motorista:
            return (self.__id_motorista,self.__CPF_passageiro, self.__id_corrida, self.__avaliacao_condutor, 
                    self.__avaliacao_veiculo,self.__data_inicio, self.__data_fim, self.__origem,
                    self.__destino,self.__tarifa, self.__distancia)
    
    def __str__(self):
        return f""" ---------------Corrida---------------
        id_motorista:\t{self.__id_motorista}
        CPF_passageiro:\t{self.__CPF_passageiro}
        id_corrida:\t{self.__id_corrida}
        avaliacao_condutor:\t{self.__avaliacao_condutor}
        avaliacao_veiculo:\t{self.__avaliacao_veiculo}
        data_inicio:\t{self.__data_inicio}
        data_fim:\t{self.__data_fim}
        origem:\t{self.__origem}
        destino:\t{self.__destino}
        tarifa:\t{self.__tarifa}
        distancia:\t{self.__distancia}"""