from tkinter import *
from tkinter import ttk

# cores
cor1 = "#feffff"  # Branco
cor2 = "#38576b"  # Azul
cor3 = "#ECEFF1"  # Cinza
cor4 = "#FFAB40"  # Laranja
fundo = "#3b3b3b"  # Preto

altura = 2

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=fundo)

# Criando frames
frame_display = Frame(janela, width=235, height=50, bg=cor2)
frame_display.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando Label (display)
equacao = ''

def entrar_valor(entrada):
    global equacao
    equacao = equacao + str(entrada)
    valor_texto.set(equacao)
def resultado():
    global equacao
    result = eval(equacao)
    valor_texto.set(result)

def clean():
    global equacao
    equacao = ''
    valor_texto.set('0')

valor_texto = StringVar()
valor_texto.set("0")
app_label = Label(frame_display, textvariable = valor_texto, width=16, height=2, padx= 7, relief=FLAT, anchor="e", justify=RIGHT, bg=cor2, fg=cor1, font='Ivy 17 bold')
app_label.place(x=0, y=0)

# Criando botões
fonte_botao = 'Ivy 13 bold'  # Define a fonte para os botões

b_clear = Button(frame_corpo, command= lambda: clean(), text="C", width=11, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)
b_porcentagem = Button(frame_corpo, command= lambda: entrar_valor('%'), text="%", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_porcentagem.place(x=118, y=0)
b_dividir = Button(frame_corpo, command= lambda: entrar_valor('/'), text="/", width=5, height=altura, bg=cor4, fg=cor1, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_dividir.place(x=177, y=0)
b_7 = Button(frame_corpo, command= lambda: entrar_valor('7'), text="7", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=52)
b_8 = Button(frame_corpo, command= lambda: entrar_valor('8'), text="8", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)
b_9 = Button(frame_corpo, command= lambda: entrar_valor('9'), text="9", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=52)
b_mult = Button(frame_corpo, command= lambda: entrar_valor('*'), text="X", width=5, height=altura, bg=cor4, fg=cor1, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_mult.place(x=177, y=52)
b_4 = Button(frame_corpo, command= lambda: entrar_valor('4'), text="4", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104)
b_5 = Button(frame_corpo, command= lambda: entrar_valor('5'), text="5", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)
b_6 = Button(frame_corpo, command= lambda: entrar_valor('6'), text="6", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=104)
b_sub = Button(frame_corpo, command= lambda: entrar_valor('-'), text="-", width=5, height=altura, bg=cor4, fg=cor1, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_sub.place(x=177, y=104)
b_1 = Button(frame_corpo, command= lambda: entrar_valor('1'), text="1", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=156)
b_2 = Button(frame_corpo, command= lambda: entrar_valor('2'), text="2", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=156)
b_3 = Button(frame_corpo, command= lambda: entrar_valor('3'), text="3", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=156)
b_soma = Button(frame_corpo, command= lambda: entrar_valor('+'), text="+", width=5, height=altura, bg=cor4, fg=cor1, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_soma.place(x=177, y=156)
b_0 = Button(frame_corpo, command= lambda: entrar_valor('0'), text="0", width=11, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=208)
b_ponto = Button(frame_corpo, command= lambda: entrar_valor('.'), text=".", width=5, height=altura, bg=cor3, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=118, y=208)
b_igual = Button(frame_corpo, command= lambda: resultado(), text="=", width=5, height=altura, bg=cor4, fg=cor1, font=fonte_botao, relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=208)


janela.mainloop()
entrar_valor()