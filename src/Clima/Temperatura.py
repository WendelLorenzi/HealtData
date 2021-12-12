# coding=utf-8

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

from src.Clima.Umidade import Umidade

class Clima:
    def __init__(self, patch, regiao):
        self.patch= patch
        self.regiao= regiao
        self.main()

    def getPatch(self):
        return self.patch
    
    def getRegiao(self):
        return self.regiao

    def carrega(self):
        ##Carregando os dados do dataset na memória
        df= pd.read_csv(self.getPatch(), sep=",", encoding="ISO-8859-1", skiprows=1)

        #filtrando apenas as colunas desejadas
        dfValues= df.filter(items=['Data Medicao', 'TEMPERATURA MEDIA', 'UMIDADE DO AR DIARIA'])

        #convertendo a coluna 1 para datetime.data
        dfValues['Data Medicao']= pd.to_datetime(dfValues['Data Medicao'], format='%Y-%m-%d')
        #Seleciona um intervalo de 10 anos
        selecao= ((dfValues['Data Medicao'] >= '2010') & (dfValues['Data Medicao'] <= '2019'))
        dfFiltrado= dfValues[selecao]
        return dfFiltrado

    def filtro(self, dfFiltrado):
        #Removendo valores maiores que 50 graus e umidade maior que 100%
        df_aux = dfFiltrado.loc[(dfFiltrado['TEMPERATURA MEDIA'] > 50) | (dfFiltrado['UMIDADE DO AR DIARIA'] > 100)]
        dfFiltrado = dfFiltrado.drop(df_aux.index)

        # Excluindo dados vazios
        dfFiltrado['TEMPERATURA MEDIA'].replace('', np.nan, inplace=True)
        dfFiltrado['UMIDADE DO AR DIARIA'].replace('', np.nan, inplace=True)
        dfFiltrado.dropna(subset=['TEMPERATURA MEDIA', 'UMIDADE DO AR DIARIA'], inplace=True)

        #Passa a coluna como vetor e elimina dados inconsistentes
        dfFiltrado[['TEMPERATURA MEDIA']].replace([np.inf, -np.inf], np.nan, inplace=True)
        temp_y= dfFiltrado[['TEMPERATURA MEDIA']]
        #print(type(temp_y))
        dfFiltrado[['UMIDADE DO AR DIARIA']].replace([np.inf, -np.inf], np.nan, inplace=True)
        umidade= dfFiltrado[['UMIDADE DO AR DIARIA']]
        data= dfFiltrado[['Data Medicao']]
        df2 = pd.DatetimeIndex(dfFiltrado['Data Medicao']).year

        #Cria uma variavel auxiliar, tal variavel equivale aos indices do dataset, sendo o menor indice a data inicial e o maior indice a data final
        det_x = np.arange(0,len(temp_y),1)

        return det_x, temp_y, data, umidade, df2

    def modelo(self, det_x, dataClima):
        #Criando e treinando o modelo
        model = LinearRegression()
        model.fit(det_x.reshape(-1, 1), dataClima)

        # extrair coeficientes
        slope = model.coef_
        intercept = model.intercept_

        return slope, intercept

    #Exportando os resultados
    def figTemperatura(self, data, temp, reg, dataYear):
        fig, (ax1, ax2)= plt.subplots(1, 2, figsize=(14,8))
        ax1.plot(data, temp)
        ax2.plot(dataYear, temp)
        ax1.set(title='Temperauta x Ano | Região: %s \n Temperatura mediana: %.2f ºC' %(self.getRegiao(), reg.median()), xlabel=('Anos'), ylabel='Temperatura')
        ax2.set(title='Temperauta x Ano | Região: %s' %self.getRegiao(), xlabel= 'Anos', ylabel='Temperatura')
        fig.tight_layout()
        fig.savefig('src/Graficos/Temperaturafigure.jpeg', format='jpeg')

    def main(self):
        detx, temp, data, umidade, dfyear= self.filtro(self.carrega())
        At, Bt= self.modelo(detx, temp)
        Au, Bu= self.modelo(detx, umidade)
        regT= (Bt + (temp * At)) #Ax + B ou B + Ax
        regU= (Bu + (umidade * Au))
        self.figTemperatura(data, temp, regT, dfyear)
        #Umidade(data, umidade, regU, self.getRegiao())
        

