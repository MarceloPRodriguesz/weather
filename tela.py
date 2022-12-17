import tkinter
import random
from tkinter import *
from tkinter import ttk 
from weather import pesquisa_clima, pesquisa_temperatura
from PIL import Image, ImageTk
# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"

def main():
    # Metodos
    def altera_temperatura(clima, temperatura):
        tempo_atual.config(text= clima, fg=co0 )
        valor_temperatura.config(text= temperatura, fg=co0 )
            
    def temperatura_atual():
        city = campo_cidade.get()
        clima = pesquisa_clima(city)
        temperatura = pesquisa_temperatura(city)
        altera_temperatura(clima, temperatura)
        campo_cidade.delete(0,END)
            
    # definindo tamanho de janela 
    janela = Tk()
    janela.title('Weather')
    janela.geometry('260x200')
    janela.configure(bg=fundo)
    
    
    # Personalizando janela
    # Label de titulo e imagem do titulo
    titulo = Label(janela, text="WEATHER ", height=2, anchor='center', font=('Consolas 20 bold'), bg=fundo, fg=co0)
    titulo.place(x=20, y=10)
    icone_termometro = Image.open("Imagens\hermometro.png")
    icone_termometro = icone_termometro.resize((60,60), Image.ANTIALIAS)
    icone_termometro = ImageTk.PhotoImage(icone_termometro)
    imagem_titulo = Label(image=icone_termometro, bg=fundo, fg=co0,anchor=CENTER, relief="flat")
    imagem_titulo.place(x=130, y=10)
        
    # Criando campo de texto
    campo_cidade = Entry(janela, width=25)
    campo_cidade.place(x=20, y=110)
    campo_cidade.focus()
    
    # Criando botão de pesquisa
    icone_lupa = Image.open('Imagens\lupa.png')
    icone_lupa = icone_lupa.resize((20,20), Image.ANTIALIAS)
    icone_lupa = ImageTk.PhotoImage(icone_lupa)
    botao_lupa = Button(janela, width=22, command=temperatura_atual, image=icone_lupa, compound=CENTER, bg=fundo, fg=co0,
                        font=('Ivy 10 bold'), anchor=CENTER, relief="flat")
    botao_lupa.place(x=200, y=109)
    
    # label de temperatura atual e graus Celcius
    tempo_atual = Label(janela, text='', anchor='center', font=('Consolas 11 bold'), bg=fundo, fg=fundo )
    tempo_atual.place(x=20, y=140)
    valor_temperatura = Label(janela, text='', anchor='center', font=('Consolas 9 bold'), bg=fundo, fg=fundo )
    valor_temperatura.place(x=20, y=160)

    # janela executando infinitamente
    janela.mainloop()

main()
