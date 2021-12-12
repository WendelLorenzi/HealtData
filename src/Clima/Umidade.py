import matplotlib.pyplot as plt
import numpy as np

class Umidade:
    def __init__(self, data, umidade, reg, regiao):
        self.data= data
        self.umidade= umidade
        self.reg= reg
        self.regiao= regiao
        self.main()

    def getData(self):
        return self.data
    
    def getUmidade(self):
        return self.umidade
    
    def getReg(self):
        return self.reg
    
    def getRegiao(self):
        return self.regiao

    def main(self):
        figU= plt.figure(num=6, figsize=(14,8))
        figU= plt.plot(self.getData(), self.getUmidade())
        figU= plt.title('Umidade x Anos | Região: %s' %(self.getRegiao()))
        figU= plt.xlabel('Anos ')
        figU= plt.ylabel('Umidade (%)')
        figU= plt.savefig('src/Graficos/Umidadefig.jpeg', format='jpeg')
