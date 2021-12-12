# coding=utf-8

from tkinter import *
from plugin import Conecta

class Tela_Clima:
    def __init__(self):
        root= Tk()
        root.geometry("850x650")
        root.title("HealtData")
        root.configure(background='#4876FF')

        self.containerMaster= Frame(root)
        self.containerMaster.place(relx=0.02, rely=0.03, relheight=0.95, relwidth=0.96)
        self.containerMaster.configure(relief=GROOVE)
        self.containerMaster.configure(borderwidth='5')
        self.containerMaster.configure(width=850)
        self.containerMaster.configure(background='#C1CDCD')

        self.MensagemIni= Message(self.containerMaster)
        self.MensagemIni.place(relx=0.00, rely=0.00, relheight=0.1, relwidth=1.0)
        self.MensagemIni.configure(text='''Projeto HealtData''')
        self.MensagemIni.configure(font=("Times New Roman", 20, "bold"))
        self.MensagemIni.configure(width=500)
        self.MensagemIni.configure(background='#C1CDCD')

        self.img= PhotoImage(file="/home/wendel/Área de Trabalho/Projects/HealtData/logoHD.png")
        self.labelLogo= Label(self.containerMaster, image=self.img)
        self.labelLogo.place(relx=0.37, rely=0.08)

        self.LabelCheckSex= Label(self.containerMaster, text='Sexo', anchor='nw')
        self.LabelCheckSex.place(relx=0.04, rely=0.40)
        self.CheckvarSex= StringVar()
        self.Masculino= Checkbutton(self.containerMaster, text = "Masculino", variable = self.CheckvarSex, onvalue = 'M', offvalue = 0)
        self.Masculino.place(relx=0.04, rely=0.43)
        self.Feminino= Checkbutton(self.containerMaster, text = "Feminino", variable = self.CheckvarSex, onvalue = 'F', offvalue = 0)
        self.Feminino.place(relx=0.04, rely=0.46)

        self.LabelCheckSex= Label(self.containerMaster, text='Idade', anchor='nw')
        self.LabelCheckSex.place(relx=0.18, rely=0.40)
        self.idade= Entry(self.containerMaster, bd=4)
        self.idade.place(relx=0.18, rely=0.43)


        self.LabelCheckRegiao= Label(self.containerMaster, text='Região', anchor='nw')
        self.LabelCheckRegiao.place(relx=0.43, rely=0.40)
        self.CheckvarRegiao= StringVar()
        self.Cascavel= Checkbutton(self.containerMaster, text = "Cascavel", variable = self.CheckvarRegiao, onvalue = 'Cascavel', offvalue = 0)
        self.Cascavel.place(relx=0.43, rely=0.43)
        self.Curitiba= Checkbutton(self.containerMaster, text = "Curitiba", variable = self.CheckvarRegiao, onvalue = 'Curitiba', offvalue = 0)
        self.Curitiba.place(relx=0.43, rely=0.46)
        self.Guarapuava= Checkbutton(self.containerMaster, text = "Guarapuava", variable = self.CheckvarRegiao, onvalue = 'Guarapuava', offvalue = 0)
        self.Guarapuava.place(relx=0.43, rely=0.49)
        self.Londrina= Checkbutton(self.containerMaster, text = "Londrina", variable = self.CheckvarRegiao, onvalue = 'Londrina', offvalue = 0)
        self.Londrina.place(relx=0.43, rely=0.52)
        self.Maringa= Checkbutton(self.containerMaster, text = "Maringa", variable = self.CheckvarRegiao, onvalue = 'Maringa', offvalue = 0)
        self.Maringa.place(relx=0.43, rely=0.55)
        self.PG= Checkbutton(self.containerMaster, text = "Ponta Grossa", variable = self.CheckvarRegiao, onvalue = 'Ponta Grossa', offvalue = 0)
        self.PG.place(relx=0.43, rely=0.58)


        self.Botao6= Button(self.containerMaster)
        self.Botao6.place(relx=0.04, rely=0.75, height=50, width=300)
        self.Botao6.configure(pady='0')
        self.Botao6.configure(text=''' Pesquisar ''')
        self.Botao6.configure(font=("Times New Roman", 10, "bold"))
        self.Botao6.configure(command= self.instancia)

        self.Botao7= Button(self.containerMaster)
        self.Botao7.place(relx=0.04, rely=0.87, height=30, width=100)
        self.Botao7.configure(pady='0')
        self.Botao7.configure(text='''SAIR ''')
        self.Botao7.configure(font=("Times New Roman", 10, "bold"))
        self.Botao7.configure(command= root.destroy)

        root.mainloop()

    def instancia(self):
        if(self.idade.get() != ''):
            Conecta(self.CheckvarRegiao.get(), self.CheckvarSex.get(), self.idade.get())

if __name__ == '__main__':
    Tela_Clima()