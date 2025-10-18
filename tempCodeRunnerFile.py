#primeira aula de python
# print(type('guto'))
# print(2,2,2,2,sep='-')

# # cont k cont c (comenta a parte celecionada )
# # cont k cont u 9desfaz o comentario)

# # TIPOS DE DADOS
# #str -> string ( texto com duplas e aspas comum ou duplas)
# #int -> inteiro ( numeros inteiros )
# # float -> flutuante (10.02)
# '''  
# variaveis sao usadas para salvar algo na me,oria do computador .
# PEP8:inicie variaveis com numeros e underline 
# o sinal '=' e operador de atribuicao
# '''

# nome = 'guto'
# print ('seu nome e',nome,)

import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk #Pillow

#configurar aparência
ctk.set_appearance_mode('dark')#light,#dark,system

#Janela principal
janela = ctk.CTk()
janela.geometry('600x500')
janela.title('Exemplo com customTkinter')

#Frame cadastro
frame_cadastro = ctk.CTkFrame(janela)
frame_cadastro.place(x=20,y=20)

btn_cadastro = ctk.CTkButton(frame_cadastro,text='Cadastro')
btn_cadastro.place(x=30,y=100)

frame_imagem = ctk.CTkFrame(janela)
frame_imagem.place(x=250,y=20)

#Carregar imagem

# img = Image.open('icon.png')#abrir a imagem
# img = img.resize((200,200))#Altura e larguara da img
# imagem = ImageTk.PhotoImage(img)#Converte a img

# label_imagem = ctk.CTkLabel(frame_imagem,image=imagem,text='')
# label_imagem.place(x=50,y=20)

# https://fromsmash.com/praticacustom



# https://fromsmash.com/praticacustom





# https://fromsmash.com/praticacustom

