from tkinter import*
from math import*

janela=Tk()
janela.title("Calculadora Cientifica")
janela.geometry("445x489")
janela.resizable(False, False)
janela.iconbitmap(r'calculator.ico')
#As variáveis que definem os tamanhos dos botões
al=3
an=11

#As funções que  permitem a execução dos cálculos
def bclick(num):
	global operador
    
	operador= operador+str(num)
	a.set(operador)

def clear():
	global operador
	operador=" "
	a.set(operador)

def operacao():
	global operador
	try:
		opera=eval(operador)
	except:
		clear()
		opera=("ERROR")
	a.set(opera)

a=StringVar()
operador=""

#os botões com seus respectivos nomes, em ordem
botraiz=Button(janela, text="√", width=an, height=al, command=lambda:bclick("sqrt"))
botraiz.place(x=1, y=85) #o metodo .place permite configurar os widgets com coordenadas. Enquanto o metodo .grid organiza os widgets como numa matriz
botnexpo=Button(janela, text="EXP", width=an, height=al, command=lambda:bclick("**"))
botnexpo.place(x=90, y=85)
botnlog=Button(janela, text="log", width=an, height=al, command=lambda:bclick("log10"))
botnlog.place(x=179, y=85)
botnln=Button(janela, text="ln", width=an, height=al, command=lambda:bclick("log"))
botnln.place(x=268, y=85)
botnsin=Button(janela, text="sin", width=an, height=al, command=lambda:bclick("sin(radians"))
botnsin.place(x=357, y=85)

botncos=Button(janela, text="cos", width=an, height=al, command=lambda:bclick("cos(radians"))
botncos.place(x=1, y=143)
botntan=Button(janela, text="tan", width=an, height=al, command=lambda:bclick("tan(radians"))
botntan.place(x=90, y=143)
botnarcsin=Button(janela, text="arcsin", width=an, height=al, command=lambda:bclick("degrees(asin"))
botnarcsin.place(x=179, y=143)
botnarccos=Button(janela, text="arccos", width=an, height=al, command=lambda:bclick("degrees(acos"))
botnarccos.place(x=268, y=143)
botnrctan=Button(janela, text="arctan", width=an, height=al, command=lambda:bclick("degrees(atan"))
botnrctan.place(x=357, y=143)

botnsec=Button(janela, text="sec", width=an, height=al, command=lambda:bclick("1/cos(radians"))
botnsec.place(x=1, y=201)
botncsc=Button(janela, text="csc", width=an, height=al, command=lambda:bclick("1/sin(radians"))
botncsc.place(x=90, y=201)
botncot=Button(janela, text="cot", width=an, height=al, command=lambda:bclick("1/tan(radians"))
botncot.place(x=179, y=201)
botnpariz=Button(janela, text="(", width=an, height=al, command=lambda:bclick("("))
botnpariz.place(x=268, y=201)
botnparde=Button(janela, text=")", width=an, height=al, command=lambda:bclick(")"))
botnparde.place(x=357, y=201)

botn7=Button(janela, text="7", width=an, height=al, command=lambda:bclick(7))
botn7.place(x=1, y=259)
botn8=Button(janela, text="8", width=an, height=al, command=lambda:bclick(8))
botn8.place(x=90, y=259)
botn9=Button(janela, text="9", width=an, height=al, command=lambda:bclick(9))
botn9.place(x=179, y=259)
botnAC=Button(janela, text="AC", width=an, height=al, command=clear)
botnAC.place(x=268, y=259)
botnDEL=Button(janela, text="DEL", width=an, height=al, command=lambda:bclick("DEL"))
botnDEL.place(x=357, y=259)

botn4=Button(janela, text="4", width=an, height=al, command=lambda:bclick(4))
botn4.place(x=1, y=317)
botn5=Button(janela, text="5", width=an, height=al, command=lambda:bclick(5))
botn5.place(x=90, y=317)
botn6=Button(janela, text="6", width=an, height=al, command=lambda:bclick(6))
botn6.place(x=179, y=317)
botnmultip=Button(janela, text="x", width=an, height=al, command=lambda:bclick("*"))
botnmultip.place(x=268, y=317)
botndivi=Button(janela, text="÷", width=an, height=al, command=lambda:bclick("/"))
botndivi.place(x=357, y=317)

botn1=Button(janela, text="1", width=an, height=al, command=lambda:bclick(1))
botn1.place(x=1, y=375)
botn2=Button(janela, text="2", width=an, height=al, command=lambda:bclick(2))
botn2.place(x=90, y=375)
botn3=Button(janela, text="3", width=an, height=al, command=lambda:bclick(3))
botn3.place(x=179, y=375)
botnsuma=Button(janela, text="+", width=an, height=al, command=lambda:bclick("+"))
botnsuma.place(x=268, y=375)
botnresta=Button(janela, text="-", width=an, height=al, command=lambda:bclick("-"))
botnresta.place(x=357, y=375)

botn0=Button(janela, text="0", width=an, height=al, command=lambda:bclick(0))
botn0.place(x=1, y=433)
botncoma=Button(janela, text=",", width=an, height=al, command=lambda:bclick("."))
botncoma.place(x=90, y=433)
botnpi=Button(janela, text="π", width=an, height=al, command=lambda:bclick("pi"))
botnpi.place(x=179, y=433)
botnporc=Button(janela, text="%", width=an, height=al, command=lambda:bclick("%"))
botnporc.place(x=268, y=433)
botnresl=Button(janela, text="=", width=an, height=al, command=operacao)
botnresl.place(x=357, y=433)

sair=Entry(janela, font=("Arial",20,"bold"), textvariable=a, width=22, bd=20, insertwidth=5, bg="antique white", justify="right")
sair.pack()

janela.mainloop()