# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:06:45 2019

@author: Cristian
"""

import CRUD as CRUD

#%%

class InformacoesCorrida(CRUD):
    
    banco = None
    cursor = None
    tabela = "InformacoesCorrida"

    def __init__(self,dados=None):
        InformacoesCorrida.banco = super().banco
        InformacoesCorrida.cursor = super().cursor
        if dados == None:
            self.__CPF_condutor          = None
            self.__Nome                  = None
            self.__CPF_passageiro        = None
            self.__nome                  = None
            self.__origem                = None
            self.__destino               = None
            self.__distancia             = None
            self.__Valor                 = None
            self.__Duracao               = None
            self.__renavan               = None
            self.__placa                 = None
            self.__marca                 = None
            self.__ano                   = None
        else:   
            self.fromTuple(dados)     
            
    def ler(self,id=None):
        if id:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE CPF_condutor=%s",(id,))    
        elif self.__CPF_condutor != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE CPF_condutor=%s",(self.__CPF_condutor,))
        else:
            raise Exception("Necessário passar o id_motorista")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)
    
    def fromTuple(self,dados):
        if len(dados) == 13:
            self.__CPF_condutor          = dados[0]
            self.__Nome                  = dados[1]
            self.__CPF_passageiro        = dados[2]
            self.__nome                  = dados[3]
            self.__origem                = dados[4]
            self.__destino               = dados[5]
            self.__distancia             = dados[6]
            self.__Valor                 = dados[7]
            self.__Duracao               = dados[8]
            self.__renavan               = dados[9]
            self.__placa                 = dados[10]
            self.__marca                 = dados[11]
            self.__ano                   = dados[12]
            
    def toTuple(self):
        if self.__CPF_condutor:
            return (self.__CPF_condutor,self.__Nome,self.__CPF_passageiro,self.__nome,
                    self.__origem,self.__destino,self.__distancia,self.__Valor,
                    self.__Duracao,self.__renavan,self.__placa,self.__marca,self.__ano)
    
    def __str__(self):
        return f""" ---------------Corrida---------------
        CPF_condutor:\t{self.__CPF_condutor}
        Nome:\t{self.__Nome}
        CPF_passageiro:\t{self.__CPF_passageiro}
        nome:\t{self.__nome}
        origem:\t{self.__origem}
        destino:\t{self.__destino}
        distancia:\t{self.__distancia}
        Valor:\t{self.__Valor}
        Duracao:\t{self.__Duracao}
        renavan:\t{self.__renavan}
        placa:\t{self.__placa}
        marca:\t{self.__marca}
        ano:\t{self.__ano}"""