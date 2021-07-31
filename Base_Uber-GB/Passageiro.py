# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:40:53 2019

@author: Cristian
"""

import CRUD as CRUD

#%%

class Passageiro(CRUD):
    
    banco = None
    cursor = None
    tabela = "Passageiro"

    def __init__(self,dados=None):
        Passageiro.banco = super().banco
        Passageiro.cursor = super().cursor
        if dados == None:
            self.__CPF_passageiro   = None
            self.__nome             = None
            self.__telefone         = None
            self.__data_cadastro    = None
        else:
            self.fromTuple(dados)
    
    @property
    def CPF_passageiro(self):
        return self.__CPF_passageiro
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
        self.atualizar()

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone
        self.atualizar()
        
    @property
    def data_cadastro(self):
        return self.__data_cadastro
    
    @data_cadastro.setter
    def data_cadastro(self,data_cadastro):
        self.__data_cadastro = data_cadastro
        self.atualizar()
    
    def novo(self, CPF_passageiro=None,nome=None,telefone=None,data_cadastro=None):
        self.cursor.execute(f"INSERT INTO {self.tabela} (CPF_passageiro,nome,telefone,data_cadastro) values (%s,%s,%s,%s)",(CPF_passageiro,nome,telefone,data_cadastro))
        self.banco.commit()
        self.CPF_passageiro = self.cursor.lastrowid
        
    def ler(self,id=None):
        if id:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE CPF_passageiro=%s",(id,))    
        elif self.__nome != None:
            self.cursor.execute(f"SELECT * FROM {self.tabela} WHERE CPF_passageiro=%s",(self.__CPF_passageiro,))
        else:
            raise Exception("Necessário passar o CPF_passageiro")
        resultado = self.cursor.fetchone()
        self.fromTuple(resultado)

    def atualizar(self):
        if self.__CPF_passageiro:
            self.cursor.execute(f"UPDATE {self.tabela} SET nome=%s, telefone=%s, data_cadastro=%s WHERE CPF_passageiro=%s",(self.__nome, self.__telefone, self.__data_cadastro, self.__CPF_passageiro,))
            self.banco.commit()
            return self.cursor.rowcount
        else:
            raise Exception("É necessário possuir um CPF_passageiro para atualizar")
    
    def apagar(self):
        if self.__CPF_passageiro:
            pass # SQL apagar e zerar o id
        else:
            raise Exception("Necessário CPF_passageiro para remover")
    
    def fromTuple(self,dados):
        if len(dados) == 4:
            self.__CPF_passageiro = dados[0]
            self.__nome = dados[1]
            self.__telefone= dados[2]
            self.__data_cadastro= dados[3]

    def toTuple(self):
        if self.__CPF_passageiro:
            return (self.__CPF_passageiro,self.__nome, self.__telefone, self.__data_cadastro)
    
    def __str__(self):
        return f""" ---------------Passageiro---------------
        CPF_passageiro:\t{self.__CPF_passageiro}
        nome:\t{self.__nome}
        telefone:\t{self.__telefone}
        data_cadastro:\t{self.__data_cadastro}"""