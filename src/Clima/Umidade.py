import matplotlib.pyplot as plt

class Umidade:
    def __init__(self, data, umidade, reg, regiao, dfYear):
        self.data= data
        self.umidade= umidade
        self.reg= reg
        self.regiao= regiao
        self.dfY= dfYear
        self.main()

    def getData(self):
        return self.data
    
    def getUmidade(self):
        return self.umidade
    
    def getReg(self):
        return self.reg
    
    def getRegiao(self):
        return self.regiao
    
    def getDfYear(self):
        return self.dfY

    def main(self):
        fig, (ax1, ax2)= plt.subplots(1, 2, num=6, figsize=(14,8))
        ax1.plot(self.getData(), self.getUmidade())
        ax2.plot(self.getDfYear(), self.getUmidade())
        ax1.set(title=('Umidade x Anos | Região: %s \n Umidade mediana: %.2f ºC' %(self.getRegiao(), self.getReg().median())), xlabel=('Anos'), ylabel=('Umidade (%)'))
        ax2.set(title=('Umidade x Anos | Região: %s' %(self.getRegiao())), xlabel= ('Anos'), ylabel=('Umidade (%)'))
        fig.tight_layout()
        fig.savefig('src/Graficos/Umidadefig.jpeg', format='jpeg')
