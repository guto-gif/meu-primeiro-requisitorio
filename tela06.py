import tkinter as tk 
from tkinter import ttk
tabela ={}

janela = tk.Tk()
janela.title('tela')
janela.geometry('700x700')
janela.grid_columnconfigure(0,weight=1)# (0) AJUSTA DA COLUNA DO GRID NA TELA *** WEIGHT OS FRAMES AUMENTA DE DIMINUI CONFORME A JANELA

def adicionar():
   nome = entray_nome.get()
   idade = entray_emial.get()
   if nome and idade:
      tabela.insert("",tk.END,values=("",nome,idade))
      
frame01 = tk.LabelFrame(text='DADOS DO CLIENTE',bg="#67C2E6")
frame01.grid(pady=5,sticky='n,s,e,w')#stinky para alinha ou organisar as entry na mesma linha

label_nome= tk.Label(frame01,text='NOME')
label_nome.grid(row=0,column=0,padx=5,pady=5)

entray_nome=tk.Entry(frame01,text='')
entray_nome.grid(row=0,column=1,padx=5,pady=5)

label_emial= tk.Label(frame01,text='Email:')
label_emial.grid(row=1,column=0,padx=5,pady=5)

entray_emial=tk.Entry(frame01,text='')
entray_emial.grid(row=1,column=1,padx=5,pady=5)

label_telefone= tk.Label(frame01,text='TELEFONE:')
label_telefone.grid(row=2,column=0,padx=5,pady=5)

entray_telefone=tk.Entry(frame01,text='')
entray_telefone.grid(row=2,column=1,padx=5,pady=5)

label_pesquisar= tk.Button(frame01,text='PESQUISAR:',bd=6,bg="#5DA1E0",fg='white')
label_pesquisar.grid(row=0,column=3,padx=6,pady=5)

entray_pesquisar=tk.Entry(frame01,text='')
entray_pesquisar.grid(row=0,column=4,padx=5,pady=5)

label_cadastra= tk.Button(frame01,text='CADASTRA (Enter):',width=15,bd=6,bg="#5DA1E0",fg='white',command=adicionar)
label_cadastra.grid(row=3,column=0,padx=5,pady=5)
label_limpar= tk.Button(frame01,text='LIMPAR(F2):',width=15,bd=6,bg="#5DA1E0",fg='white')
label_limpar.grid(row=3,column=1,padx=5,pady=5)
label_excluir= tk.Button(frame01,text='EXCLUIR(delete):',width=15,bd=6,bg="#5DA1E0",fg='white')
label_excluir.grid(row=3,column=2,padx=5,pady=5)
label_apagar= tk.Button(frame01,text='DESFAZER DELETE:',width=15,bd=6,bg="#5DA1E0",fg='white')
label_apagar.grid(row=3,column=3,padx=5,pady=5)
label_salvar= tk.Button(frame01,text='SALVAR:    ',width=15,bd=6,bg="#5DA1E0",fg='white')
label_salvar.grid(row=3,column=4,padx=5,pady=5)

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
frame_btn.place(x=10,y=450)
# butao=tk.Button(frame_cadastro,text='',command=adicionar)
# butao.grid(row=10, column=3, pady=6,padx=5,sticky='wens')
btn_cadastro=tk.Button(frame_btn,text='cadastro',command=adicionar,bd=4,bg="#79BEE6")
btn_cadastro.grid(row=0,column=0,padx=5)

btn_excluir=tk.Button(frame_btn,text='excluir',bd=4,bg="#79BEE6")
btn_excluir.grid(row=0,column=1,padx=5)








janela.mainloop()