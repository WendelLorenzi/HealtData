# coding=utf-8

from src.Clima.Temperatura import Clima
from src.SRAG.srag import Srag
from src.SRAG.amostras import Amostras
import matplotlib.pyplot as plt

class Centralizador:
    def __init__(self, list):
        self.regiao= list[0]
        self.sex= list[1]
        self.idade= list[2]
        self.main()
    
    def getRegiao(self):
        return self.regiao
    
    def getGenero(self):
        return self.sex
    
    def getIdade(self):
        return int(self.idade)

    def endereco_dataset(self, regiao):
        if(regiao == 'Cascavel'):
            #Estação de Marechal Candido Rondon
            patch= 'datasets/A820_Temp_MAL. CANDIDO RONDON_2006-2021.csv'
            return patch
        elif(regiao == 'Curitiba'):
            patch= 'datasets/A807_Temp_CURITIBA_2003-2021.csv'
            return patch  
        elif(regiao == 'Guarapuava'):
            #Estação de Inacio Martins
            patch= 'datasets/A823_Temp_INACIO MARTINS_2006-2021.csv'
            return patch
        elif(regiao == 'Londrina'):
            #Estação de Nova Fatima
            patch= 'datasets/A842_Temp_NOVA FATIMA_2007-2021.csv'
            return patch
        elif(regiao == 'Maringa'):
            patch= 'datasets/A835_Temp_MARINGA_2006-2021.csv'
            return patch
        elif(regiao == 'Ponta Grossa'):
            #Estação de Castro
            patch= 'datasets/A819_Temp_CASTRO_2006-2021.csv'
            return patch
        else: raise Exception('Erro na regiao')


    def main(self):
        patch= self.endereco_dataset(self.getRegiao())
        Clima(patch, self.getRegiao())
        doenca = Srag(self.getRegiao(), self.getGenero(), self.getIdade())
        doenca_amostra = Amostras(doenca)

        ##Grafico de linha sobre o numero total de casos
        doenca.graficoLinha()
        #Grafico de barras com normalidade
        doenca.graficoBarras()
        #Grafico Regressao linear Temperatura
        doenca_amostra.rlAmostraTemperatura()
        #Grafico Regressao linear Umidade
        doenca_amostra.rlAmostraUmidade()
        plt.show()
