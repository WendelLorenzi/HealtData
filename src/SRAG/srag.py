# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.reshape.concat import concat
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class Srag:
    def __init__(self, regiao, sexo, idade):
        self.dadosSrag = pd.read_csv('datasets/dadosSRAG.csv', sep=';', decimal=',', encoding="ISO-8859-1")
        self.dadosSragParana = self.dadosSrag.loc[self.dadosSrag['SIGLA'] == "PR"]
        self.dadosSragParana['DT_NOTIFIC'] = pd.to_datetime(self.dadosSragParana['DT_NOTIFIC'])
        self.dadosSragParana['DT_NASC'] = pd.to_datetime(self.dadosSragParana['DT_NASC'])
        self.dadosSragParana['DT_OBITO'] = pd.to_datetime(self.dadosSragParana['DT_OBITO'])
        self.regiao = regiao
        self.sexo = sexo
        self.idade = idade
        self.faixaEtaria = self.setFaixaEtaria()

    def getNomeRegiao (self):
        return self.regiao

    def setFaixaEtaria(self):
        if self.idade < 15:
            return "Criança"
        elif (self.idade >= 15) & (self.idade < 25):
            return "Jovem"
        elif (self.idade >= 25) & (self.idade < 65):
            return "Adulto"
        else: return "Idoso"
    
    def getRegiao(self):
        return self.dadosSragParana.loc[self.dadosSragParana['REGIAO'] == self.regiao]
    
    def getCurados(self):
        return self.getRegiao().loc[(self.getRegiao()['DT_OBITO'].isnull()) | (self.getRegiao()['EVOLUCAO'] == 'Cura')]
    
    def getObitos(self):
        return self.getRegiao().loc[self.getRegiao()['EVOLUCAO'] != 'Cura']
    
    def getFaixaEtaria (self):
        dados = self.getRegiao()
        return dados.loc[dados['FAIXA_ETARIA'] == self.faixaEtaria]

    def getSexo (self):
        dados = self.getFaixaEtaria()
        return dados.loc[dados['CS_SEXO'] == self.sexo]
    
    def getDados (self):
        dados = self.getSexo()
        return dados[dados['REGIAO'] == self.regiao]

    def agruparDtNotific (self, dados):
        return dados.groupby(dados['DT_NOTIFIC'].dt.year)["ID"].count()

    def agruparDtObito (self, dados):
        return dados.groupby(dados['DT_OBITO'].dt.year)["ID"].count()
    
    def agruparDtNotificMes (self, dados):
        return dados.groupby(dados['DT_NOTIFIC'].dt.month)["ID"].count()
    
    #Interação de gráficos

    def graficoLinha (self):
        casos = self.getRegiao()
        curados = self.getCurados()
        obitos = self.getObitos()

        graph = plt.figure(num=5, figsize=(14,8))
        graph = plt.plot(self.agruparDtNotific(casos), '--', color='black', label="Nro total de casos")
        graph = plt.plot(self.agruparDtNotific(curados), '-', color='blue', label="Nro total de curados")
        graph = plt.plot(self.agruparDtNotific(obitos), '-', color='red', label="Nro total de obitos")

        text = "Casos de SARS ao longo do periodo | Regiao: " + self.regiao

        graph = plt.title("Casos de SARS ao longo do periodo")
        graph = plt.ylabel("Número de casos")
        graph = plt.xlabel("Periodo (em anos)")

        graph = plt.grid()
        graph = plt.legend(loc=1)
        graph = plt.savefig('src/Graficos/GraficoLinha.jpeg', format='jpeg')

    def graficoBarras (self):
        dados = self.getDados()
        dados = self.agruparDtNotificMes(dados)
        x = np.arange(1, 13, 1)
        #Regressao Linear
        lm_model = LinearRegression()
        lm_model.fit(x.reshape(-1,1), dados.array)
        slope = lm_model.coef_
        intercept = lm_model.intercept_

        text = "Grafico: Faixa Etaria: "+self.faixaEtaria+"s"+" | sexo: "+self.sexo+ " | Região: "+self.regiao
        plt.figure(num=2, figsize=(14,8))
        plt.bar(x, dados.to_numpy(), color='b')
        plt.plot(x, (x*slope+intercept), color='red', label='Linha de Normalidade')

        plt.xlabel("Periodo (em meses)")
        plt.ylabel("Número de casos")

        plt.title(text)
        plt.legend()
        plt.savefig('src/Graficos/GraficoBarras.jpeg', format='jpeg')

    def rlAmostraTemperatura(self):
        amostras = self.getRegiaoAmostra()
        amostras = self.agruparAmostras(amostras)
        doencas = self.getDados()
        doencas = self.agruparDtNotificMes(doencas)

        lm_model2 = LinearRegression()
        lm_model2.fit(doencas.to_numpy().reshape(-1,1), amostras.to_numpy())
        slope = lm_model2.coef_
        intercept = lm_model2.intercept_

        plt.figure(figsize=(14,8))
        plt.scatter(doencas.to_numpy(), amostras.to_numpy(), color='b')
        plt.plot(doencas.to_numpy(), (doencas.to_numpy()*slope+intercept), color='r')

        plt.xlabel("Numero de Casos")
        plt.ylabel("Temperatura (ºC)")

        plt.title("Regressão Linear: Temperatura x Numero de Casos")

        plt.savefig('src/Graficos/RegressaoTemperatura.jpeg', format='jpeg')

