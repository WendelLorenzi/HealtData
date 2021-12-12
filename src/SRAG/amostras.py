# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.reshape.concat import concat
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class Amostras:
    def __init__(self, doenca):
        self.amostraClima = pd.read_csv('datasets/clima.csv', sep=';', decimal=',', encoding="ISO-8859-1")
        self.amostraClima['DT_NOTIFIC'] = pd.to_datetime(self.amostraClima['DT_NOTIFIC'])
        self.srag = doenca
    
    #Amostras Clima e Umidade
    def getRegiaoAmostra (self):
        return self.amostraClima.loc[self.amostraClima['REGIAO'] == self.srag.getNomeRegiao()]

    def agruparAmostrasTemperatura (self, dados):
        return dados.groupby(dados['DT_NOTIFIC'].dt.month)["TEMPERATURA"].mean()

    def agruparAmostrasUmidade (self, dados):
        return dados.groupby(dados['DT_NOTIFIC'].dt.month)["UMIDADE"].mean()

    def rlAmostraTemperatura(self):
        amostras = self.getRegiaoAmostra()
        amostras = self.agruparAmostrasTemperatura(amostras)
        doencas = self.srag.getDados()
        doencas = self.srag.agruparDtNotificMes(doencas)

        lm_model2 = LinearRegression()
        lm_model2.fit(doencas.to_numpy().reshape(-1,1), amostras.to_numpy())
        slope = lm_model2.coef_
        intercept = lm_model2.intercept_

        text = "Regressão Linear: Temperatura x Numero de Casos | Regiao: "+ self.srag.getNomeRegiao()

        plt.figure(num=3, figsize=(14,8))
        plt.scatter(doencas.to_numpy(), amostras.to_numpy(), color='b')
        plt.plot(doencas.to_numpy(), (doencas.to_numpy()*slope+intercept), color='r')

        plt.xlabel("Numero de Casos")
        plt.ylabel("Temperatura (ºC)")

        plt.title(text)

        plt.savefig('src/Graficos/RegressaoTemperatura.jpeg', format='jpeg')

    def rlAmostraUmidade(self):
        amostras = self.getRegiaoAmostra()
        amostras = self.agruparAmostrasUmidade(amostras)
        doencas = self.srag.getDados()
        doencas = self.srag.agruparDtNotificMes(doencas)

        lm_model2 = LinearRegression()
        lm_model2.fit(doencas.to_numpy().reshape(-1,1), amostras.to_numpy())
        slope = lm_model2.coef_
        intercept = lm_model2.intercept_

        text = "Regressão Linear: Umidade x Numero de Casos | Regiao: "+ self.srag.getNomeRegiao()

        plt.figure(num=4, figsize=(14,8))
        plt.scatter(doencas.to_numpy(), amostras.to_numpy(), color='b')
        plt.plot(doencas.to_numpy(), (doencas.to_numpy()*slope+intercept), color='r')

        plt.xlabel("Numero de Casos")
        plt.ylabel("Umidade Relativa do Ar")

        plt.title(text)

        plt.savefig('src/Graficos/RegressaoUmidade.jpeg', format='jpeg')
