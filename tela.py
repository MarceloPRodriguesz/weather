import tkinter
import random
from tkinter import *
from tkinter import ttk 
from weather import pesquisa_clima
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
    # definindo tamanho de janela 
    janela = Tk()
    janela.title('Weather')
    janela.geometry('260x230')
    janela.configure(bg=fundo)
    
    def altera_clima(tempo):
       # Cria label com clima atual
        clima = [tempo]
        tempo = str(clima[0])
        tempo.replace("'", "")
        tempo.replace(",", " ")
        
        
        exibe_tempo.config(text= tempo)
        
    
    def captura_cidade():
        # Variavel recebe texto digitado no campo 
        city=campo_cidade.get()
        tempo = pesquisa_clima(city)
        print(tempo)
        altera_clima(tempo)
        campo_cidade.delete(0,END)
        campo_cidade.focus()
                      
    #Metodo para receber txt digitado
    
    # Personalizando janela
    # Label de titulo
    titulo = Label(janela, text="Escolha uma cidade: ", height=2, anchor='center', font=('Arial 12 bold'), bg=fundo, fg=co0)
    titulo.place(x=20, y=40)
    
    # Criando campo de texto
    campo_cidade = Entry(janela)
    campo_cidade.place(x=20, y=80)
    campo_cidade.focus()
    
    # Criando botão de pesquisa
    icone_lupa = Image.open('Imagens\lupa.png')
    icone_lupa = icone_lupa.resize((20,20), Image.ANTIALIAS)
    icone_lupa = ImageTk.PhotoImage(icone_lupa)
    botao_lupa = Button(janela, width=22, command=captura_cidade, image=icone_lupa, compound=CENTER, bg=fundo, fg=co0,
                        font=('Ivy 10 bold'), anchor=CENTER, relief="flat")
    botao_lupa.place(x=200, y=79)
    
     # Cria label com clima atual
    exibe_tempo = Label(janela, text="", height=2, anchor='center', font=('Arial 10 bold'), bg=fundo, fg=co0)
    exibe_tempo.place(x=20, y=170)
    
    # janela executando infinitamente
    janela.mainloop()

main()

