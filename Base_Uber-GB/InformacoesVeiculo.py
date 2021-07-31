# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:55:41 2019

@author: Cristian
"""
    
import CRUD as CRUD

#%%

class InformacoesVeiculo(CRUD):
    
    banco = None
    cursor = None
    tabela = "InformacoesVeiculo"

    def __init__(self,dados=None):
        InformacoesVeiculo.banco = super().banco
        InformacoesVeiculo.cursor = super().cursor
        if dados == None:
            self.__placa                  = None
            self.__renavan                = None
            self.__modelo                 = None
            self.__marca                  = None
            self.__ano                    = None
            self.__QuantidadeCorridas     = None
            self.__QuantidadeAvalicoes    = None
            self.__Med_Avaliacao_Veiculo  = None
        else:   
            self.fromTuple(dados)     
            
    def ler(self,id=None):
        if id:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE placa=%s",(id,))    
        elif self.__placa != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE placa=%s",(self.__placa,))
        else:
            raise Exception("Necessário passar a placa")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)
    
    def fromTuple(self,dados):
        if len(dados) == 8:
            self.__placa                  = dados[0]
            self.__renavan                = dados[1]
            self.__modelo                 = dados[2]
            self.__marca                  = dados[3]
            self.__ano                    = dados[4]
            self.__QuantidadeCorridas     = dados[5]
            self.__QuantidadeAvalicoes    = dados[6]
            self.__Med_Avaliacao_Veiculo  = dados[7]
            
    def toTuple(self):
        if self.__placa:
            return (self.__placa,self.__renavan,self.__modelo,self.__marca,self.__ano,
            self.__QuantidadeCorridas,self.__QuantidadeAvalicoes,self.__Med_Avaliacao_Veiculo)
    
    def __str__(self):
        return f""" ---------------InformacoesVeiculo---------------
        Placa:\t{self.__placa}
        Renavan:\t{self.__renavan}
        Modelo:\t{self.__modelo}
        Marca:\t{self.__marca}
        Ano:\t{self.__ano}
        Quantidade Corridas:\t{self.__QuantidadeCorridas}
        Quantidade Avalicoes:\t{self.__QuantidadeAvalicoes}
        Med_Avaliacao_Veiculo:\t{self.__Med_Avaliacao_Veiculo}"""