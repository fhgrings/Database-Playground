# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:25:59 2019

@author: Cristian
"""
import CRUD as CRUD

#%%

class Condutor(CRUD):
    
    banco = None
    cursor = None
    tabela = "Condutor"

    def __init__(self,dados=None):
        Condutor.banco = super().banco
        Condutor.cursor = super().cursor
        if dados == None:
            self.__CPF_condutor = None
            self.__Nome   = None
            self.__Telefone    = None
            self.__Data_cadastro       = None
        else:
            self.fromTuple(dados)

    
    @property
    def CPF_condutor(self):
        return self.__CPF_condutor
    
    @property
    def Nome(self):
        return self.__Nome
    
    @Nome.setter
    def Nome(self,nome):
        self.__Nome = nome
        self.atualizar()

    @property
    def Telefone(self):
        return self.__Telefone
    
    @Telefone.setter
    def Telefone(self,Telefone):
        self.__Telefone = Telefone
        self.atualizar()
    
    @property
    def Data_cadastro(self):
        return self.__Data_cadastro
    
    @Data_cadastro.setter
    def Data_cadastro(self,Data_cadastro):
        self.__Data_cadastro = Data_cadastro
        self.atualizar()
    
    def novo(self, CPF_condutor=None,Nome=None,Telefone=None,Data_cadastro=None):
        self.cursor.execute(f"INSERT INTO {self.tabela} (CPF_condutor,Nome,Telefone,Data_cadastro) values (%s,%s,%s,%s)",(CPF_condutor,Nome,Telefone,Data_cadastro,))
        self.banco.commit()
        self.__CPF_condutor = self.cursor.lastrowid
        


    def ler(self,CPF_condutor=None):
        if CPF_condutor:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE CPF_condutor=%s",(CPF_condutor,))    
        elif self.__Nome != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE CPF_condutor=%s",(self.__CPF_condutor,))
        else:
            raise Exception("Necessário passar o CPF_condutor")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)

    def atualizar(self):
        if self.__CPF_condutor:
            self.cursor.execute(f"UPDATE {self.tabela} SET Nome=%s, Telefone=%s, Data_cadastro=%s WHERE CPF_condutor=%s",(self.__Nome, self.__Telefone, self.__Data_cadastro, self.__CPF_condutor,))
            self.banco.commit()
            return self.cursor.rowcount
        else:
            raise Exception("É necessário possuir um CPF_condutor para atualizar")
    
    def apagar(self):
        if self.__CPF_condutor:
            pass # SQL apagar e zerar o id
        else:
            raise Exception("Necessário CPF_condutor para remover")
    
    def fromTuple(self,dados):
        if len(dados) == 4:
            self.__CPF_condutor = dados[0]
            self.__Nome = dados[1]
            self.__Telefone= dados[2]
            self.__Data_cadastro = dados[3] 

    def toTuple(self):
        if self.__CPF_condutor:
            return (self.__CPF_condutor,self.__Nome, self.__Telefone, self.__Data_cadastro)
    
    def __str__(self):
        return f""" ---------------Condutor---------------
        CPF_condutor:\t{self.__CPF_condutor}
        Nome:\t{self.__Nome}
        Telefone:\t{self.__Telefone}
        Data_cadastro:\t{self.__Data_cadastro}"""
