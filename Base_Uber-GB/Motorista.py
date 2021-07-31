# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:26:12 2019

@author: Cristian
"""

import CRUD as CRUD

#%%

class Motorista(CRUD):
    
    banco = None
    cursor = None
    tabela = "Motorista"

    def __init__(self,dados=None):
        Motorista.banco = super().banco
        Motorista.cursor = super().cursor
        if dados == None:
            self.__id_motorista = None
            self.__CPF_condutor   = None
            self.__renavan    = None
            self.__data_inicio       = None
            self.__data_fim       = None
        else:
            self.fromTuple(dados)
    
    @property
    def id_motorista(self):
        return self.__id_motorista
    
    @property
    def CPF_condutor(self):
        return self.__CPF_condutor
    
    @CPF_condutor.setter
    def CPF_condutor(self,CPF_condutor):
        self.__CPF_condutor = CPF_condutor
        self.atualizar()

    @property
    def renavan(self):
        return self.__renavan
    
    @renavan.setter
    def renavan(self,renavan):
        self.__renavan = renavan
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
    
    def novo(self, id_motorista=None,CPF_condutor=None,renavan=None,data_inicio=None,data_fim=None):
        self.cursor.execute(f"INSERT INTO {self.tabela} (id_motorista,CPF_condutor,renavan,data_inicio,data_fim) values (%s,%s,%s,%s,%s)",(id_motorista,CPF_condutor,renavan,data_inicio,data_fim))
        self.banco.commit()
        self.id_motorista = self.cursor.lastrowid
        
    def ler(self,id=None):
        if id:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE id_motorista=%s",(id,))    
        elif self.__CPF_condutor != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE id_motorista=%s",(self.__id_motorista,))
        else:
            raise Exception("Necessário passar o id_motorista")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)

    def atualizar(self):
        if self.__id_motorista:
            self.cursor.execute(f"UPDATE {self.tabela} SET CPF_condutor=%s, renavan=%s, data_inicio=%s, data_fim=%s WHERE id_motorista=%s",(self.__CPF_condutor, self.__renavan, self.__data_inicio, self.__data_fim, self.id_motorista,))
            self.banco.commit()
            return self.cursor.rowcount
        else:
            raise Exception("É necessário possuir um id_motorista para atualizar")
    
    def apagar(self):
        if self.__id_modelo_Veiculo:
            pass # SQL apagar e zerar o id
        else:
            raise Exception("Necessário id_modelo_Veiculo para remover")
    
    def fromTuple(self,dados):
        if len(dados) == 5:
            self.__id_motorista = dados[0]
            self.__CPF_condutor = dados[1]
            self.__renavan= dados[2]
            self.__data_inicio= dados[3]
            self.__data_fim= dados[4]

    def toTuple(self):
        if self.__id_motorista:
            return (self.__id_motorista,self.__CPF_condutor, self.__renavan, self.__data_inicio, self.__data_fim)
    
    def __str__(self):
        return f""" ---------------Motorista---------------
        id_motorista:\t{self.__id_motorista}
        CPF_condutor:\t{self.__CPF_condutor}
        renavan:\t{self.__renavan}
        data_inicio:\t{self.__data_inicio}
        data_fim:\t{self.__data_fim}"""