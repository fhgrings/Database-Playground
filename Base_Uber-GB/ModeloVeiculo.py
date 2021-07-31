# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:43:57 2019

@author: Cristian
"""

import CRUD as CRUD

#%%

class ModeloVeiculo(CRUD):
    
    banco = None
    cursor = None
    tabela = "ModeloVeiculo"

    def __init__(self,dados=None):
        ModeloVeiculo.banco = super().banco
        ModeloVeiculo.cursor = super().cursor
        if dados == None:
            self.__id_modelo_Veiculo = None
            self.__modelo   = None
            self.__marca    = None
            self.__ano       = None
        else:
            self.fromTuple(dados)

    
    @property
    def id_modelo_Veiculo(self):
        return self.__id_modelo_Veiculo
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo
        self.atualizar()

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,marca):
        self.__marca = marca
        self.atualizar()
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self,ano):
        self.__ano = ano
        self.atualizar()
    
    def novo(self, id_modelo_Veiculo=None,modelo=None,marca=None,ano=None):
        self.cursor.execute(f"INSERT INTO {self.tabela} (id_modelo_Veiculo,modelo,marca,ano) values (%s,%s,%s,%s)",(id_modelo_Veiculo,modelo,marca,ano))
        self.banco.commit()
        self.__id_modelo_Veiculo = self.cursor.lastrowid
        


    def ler(self,id=None):
        if id:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE id_modelo_Veiculo=%s",(id,))    
        elif self.__modelo != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE id_modelo_Veiculo=%s",(self.__id_modelo_Veiculo,))
        else:
            raise Exception("Necessário passar o id_modelo_Veiculo")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)

    def atualizar(self):
        if self.__id_modelo_Veiculo:
            self.cursor.execute(f"UPDATE {self.tabela} SET modelo=%s, marca=%s, ano=%s WHERE id_modelo_Veiculo=%s",(self.__modelo, self.__marca, self.__ano, self.__id_modelo_Veiculo,))
            self.banco.commit()
            return self.cursor.rowcount
        else:
            raise Exception("É necessário possuir um id_modelo_Veiculo para atualizar")
    
    def apagar(self):
        if self.__id_modelo_Veiculo:
            pass # SQL apagar e zerar o id
        else:
            raise Exception("Necessário id_modelo_Veiculo para remover")
    
    def fromTuple(self,dados):
        if len(dados) == 4:
            self.__id_modelo_Veiculo = dados[0]
            self.__modelo = dados[1]
            self.__marca= dados[2]
            self.__ano= dados[3] 

    def toTuple(self):
        if self.__id_modelo_Veiculo:
            return (self.__id_modelo_Veiculo,self.__modelo, self.__marca, self.__ano)
    
    def __str__(self):
        return f""" ---------------ModeloVeiculo---------------
        id_modelo_Veiculo:\t{self.__id_modelo_Veiculo}
        modelo:\t{self.__modelo}
        marca:\t{self.__marca}
        ano:\t{self.__ano}"""