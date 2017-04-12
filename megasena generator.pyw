'''
Sorteio da mega sena
'''

from tkinter import *

app = Tk()
app.title("Mena Sena Generator")
app.geometry('550x250')
l1 = Label(app, width = 30)
l2 = Label(app, width = 30)
n = []

def escolhe():
        global n
        n.append(int(numero.get()))
        numero.delete(0, END)
        print(n)
        l2['text'] =  n
        l2.pack(side = "top")
                
def gerar():
        import random
        lista = []
        for x in n:
                lista.append(x)
        while len(lista) < 6:
                x = random.randint(1, 60)
                if x not in lista:
                    lista.append(x)
        lista.sort()
        print(lista)
        l1['text'] =  lista
        l1.pack(side = "top")

def apagar():
        global n
        n = []
        l2['text'] = n
        l2.pack(side = "top")

Label(app, text="Digitar número que queira usar: ").pack()
numero = Entry(app, width = 5)
numero.pack()

b1 = Button(app, text = "Gerar Números!", width = 15, command = gerar)
b1.pack(side = "bottom", pady = 10)    

b0 = Button (app, text = "Salvar número", width = 15, command = escolhe)
b0.pack(side ="left", padx = 10) 

b2 = Button(app, text = "Apagar Números Salvos!", width = 20, command = apagar)
b2.pack(side = "right", padx = 10)


app.mainloop()


