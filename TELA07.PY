import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


#stick=e -direita,w-esqueerda,n -topo, baixo
janela = tk.Tk()
janela.geometry('400x450')
janela.grid_columnconfigure(0,weight=1,)

def adicionar():
   nome = entry_nome.get()
   idade = label01.get()
   if nome and idade:
      tabela.insert("",tk.END,values=("",nome,idade))
      entry_nome.delete(0,tk.END)
      entry01.delete(0,tk.END)



frame_cadastro = tk.LabelFrame(text='Cadastro')
frame_cadastro.grid(sticky="nsew",padx=10,pady=10)

label_nome = tk.Label(frame_cadastro,text='nome',width=10)
label_nome.grid(row=0, column=0,padx=5,pady=5)

entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=0, column=1,padx=5,pady=5)

frame02 = tk.LabelFrame(text='Registro')
frame02.grid(sticky="nsew",padx=10,pady=10)

label01 = tk.Label(frame02,text='Idade',width=10)
label01.grid(row=0, column=0,padx=5,pady=5)

entry01 = tk.Entry(frame02)
entry01.grid(row=0, column=1,padx=5,pady=5)

frame_tabela= tk.LabelFrame(text='registros')
frame_tabela.grid(sticky='wnes')#comando sticky ,almenta e diminuir conforme o framy

#TREEVIEW
#criar a tabela com 2 colunas
tabela= ttk.Treeview(frame_tabela,columns=('nome','idade','imail','telefone'),show='headings')#o comando treeview (cria tabelas)
tabela.grid(row=2,column=0,sticky='wens')

#definir os titulos das coluna
tabela.heading('nome',text='nome') #heading -cria o titulo que vai ficar no cabeçario
tabela.heading('idade',text='idade')
tabela.heading('imail',text='imail')
tabela.heading('telefone',text='telefone')


#definir a largura das colunas
tabela.column('nome',width=100)
tabela.column('idade',width=100)
tabela.column('imail',width=100)
tabela.column('telefone',width=100)
frame_tabela.grid_columnconfigure(0,weight=1)

frame_btn=tk.LabelFrame(text='',bd=0)#bd  (0)tira as bordas do freine (1) almenta as bordas
frame_btn.place(x=10,y=400)
# butao=tk.Button(frame_cadastro,text='',command=adicionar)
# butao.grid(row=10, column=3, pady=6,padx=5,sticky='wens')
btn_cadastro=tk.Button(frame_btn,text='cadastro',command=adicionar,bd=4)
btn_cadastro.grid(row=0,column=0,padx=5)

btn_excluir=tk.Button(frame_btn,text='excluir',bd=4)
btn_excluir.grid(row=0,column=1,padx=5)







janela.mainloop()