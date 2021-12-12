# coding=utf-8

from hub import Centralizador

class Conecta:
     def __init__(self, Regiao, sex, idade):
         self.regiao= Regiao
         self.sexo= sex
         self.idade= idade
         print(self.Cria_object())

     def getSex(self):
        return self.sexo
     
     def getIdade(self):
         return self.idade
    
     def getRegiao(self):
         return self.regiao

     def Cria_object(self):
         listaObj= [self.getRegiao(), self.getSex(), self.getIdade()]
         Centralizador(listaObj)
         return listaObj