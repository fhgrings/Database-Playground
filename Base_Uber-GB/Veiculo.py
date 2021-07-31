# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:35:54 2019

@author: Cristian
"""

import CRUD as CRUD

#%%

class Veiculo(CRUD):
    
    banco = None
    cursor = None
    tabela = "Veiculo"

    def __init__(self,dados=None):
        Veiculo.banco = super().banco
        Veiculo.cursor = super().cursor
        if dados == None:
            self.__renavan              = None
            self.__placa                = None
            self.__id_modelo_veiculo    = None
        else:
            self.fromTuple(dados)

    
    @property
    def renavan(self):
        return self.__renavan
    
    @property
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self,placa):
        self.__placa = placa
        self.atualizar()

    @property
    def id_modelo_veiculo(self):
        return self.__id_modelo_veiculo
    
    @id_modelo_veiculo.setter
    def id_modelo_veiculo(self,id_modelo_veiculo):
        self.__id_modelo_veiculo = id_modelo_veiculo
        self.atualizar()
    
    def novo(self, renavan=None,placa=None,id_modelo_veiculo=None ):
        self.cursor.execute(f"INSERT INTO {self.tabela} (renavan,placa,id_modelo_veiculo) values (%s,%s,%s)",(renavan,placa,id_modelo_veiculo))
        self.banco.commit()
        self.__renavan = self.cursor.lastrowid
        


    def ler(self,id=None):
        if id:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE renavan=%s",(id,))    
        elif self.__placa != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE renavan=%s",(self.__renavan,))
        else:
            raise Exception("Necessário passar o renavan")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)

    def atualizar(self):
        if self.__renavan:
            self.cursor.execute(f"UPDATE {self.tabela} SET placa=%s, id_modelo_veiculo=%s WHERE renavan=%s",(self.__placa, self.__id_modelo_veiculo, self.__renavan,))
            self.banco.commit()
            return self.cursor.rowcount
        else:
            raise Exception("É necessário possuir um renavan para atualizar")
    
    def apagar(self):
        if self.__renavan:
            pass # SQL apagar e zerar o id
        else:
            raise Exception("Necessário renavan para remover")
    
    def fromTuple(self,dados):
        if len(dados) == 3:
            self.__renavan = dados[0]
            self.__placa = dados[1]
            self.__id_modelo_veiculo= dados[2]

    def toTuple(self):
        if self.__renavan:
            return (self.__renavan,self.__placa, self.__id_modelo_veiculo)
    
    def __str__(self):
        return f""" ---------------Veiculo---------------
        renavan:\t{self.__renavan}
        placa:\t{self.__placa}
        id_modelo_veiculo:\t{self.__id_modelo_veiculo}"""