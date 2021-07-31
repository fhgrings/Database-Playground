# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:47:05 2019

@author: Cristian
"""

import CRUD as CRUD

#%%

class InformacoesCondutor(CRUD):
    
    banco = None
    cursor = None
    tabela = "InformacoesCondutor"

    def __init__(self,dados=None):
        InformacoesCondutor.banco = super().banco
        InformacoesCondutor.cursor = super().cursor
        if dados == None:
            self.__CPF_condutor          = None
            self.__Nome                  = None
            self.__QuantidadeAvalicoes   = None
            self.__Media_avaliacoes      = None
            self.__Quantidade_Corridas   = None
            self.__Pagamento             = None
        else:   
            self.fromTuple(dados)     
            
    def ler(self,id=None):
        if id:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE CPF_condutor=%s",(id,))    
        elif self.__CPF_condutor != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE CPF_condutor=%s",(self.__CPF_condutor,))
        else:
            raise Exception("Necessário passar o CPF_condutor")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)
    
    def fromTuple(self,dados):
        if len(dados) == 6:
            self.__CPF_condutor          = dados[0]
            self.__Nome                  = dados[1]
            self.__QuantidadeAvalicoes   = dados[2]
            self.__Media_avaliacoes      = dados[3]
            self.__Quantidade_Corridas   = dados[4]
            self.__Pagamento             = dados[5]
            
    def toTuple(self):
        if self.__CPF_condutor:
            return (self.__CPF_condutor,self.__Nome,self.__QuantidadeAvalicoes,
                    self.__Media_avaliacoes,self.__Quantidade_Corridas,self.__Pagamento)
    
    def __str__(self):
        return f""" ---------------InformacoesCondutor---------------
        CPF condutor:\t{self.__CPF_condutor}
        Nome condutor:\t{self.__Nome}
        Quantidade Avalicoes:\t{self.__QuantidadeAvalicoes}
        Media Avaliacoes:\t{self.__Media_avaliacoes}
        Quantidade Corridas:\t{self.__Quantidade_Corridas}
        Pagamento:\t{self.__Pagamento}"""