# import tkinter as tk
# from tkinter import ttk
# import customtkinter as ctk
# from PIL import Image, ImageTk

# tela=ctk.CTk()
# tela._set_appearance_mode('dark')
# tela.title('exeplo')
# tela.geometry('500x500')

# #freme cadastro

# frame_cadastro=ctk.CTkFrame(tela)
# frame_cadastro.place(x=20,y=20)

# btn_cadastro= ctk.CTkButton(frame_cadastro,text='cadastro')
# btn_cadastro.place(x=30,y=100)

# frame_1=ctk.CTkFrame(tela)
# frame_1.place(x=250,y=20)

# btn_start= ctk.CTkButton(frame_cadastro,text='cadastro')
# btn_start.place(x=260,y=100)

# imagem = ImageTk.photoimage(img)
# img = Image.open('icin.png') 
# img = img.resize((50,50))('icin.png') 

# frame_imagem = ctk.CTklabel(frame_imagem,image=image)
# frame_imagem.place(x=50,y=20)
# tela.mainloop()

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

img = Image.open('icin.png')#abrir a imagem
img = img.resize((200,200))#Altura e larguara da img
imagem = ImageTk.PhotoImage(img)#Converte a img

label_imagem = ctk.CTkLabel(frame_imagem,image=imagem,text='')
label_imagem.place(x=50,y=20)



janela.mainloop()


