import tkinter as tk

def mostra_nome():
    nome = entry.get()#pega o que esta no entre
    lebel_1.config(text=F'ola, {nome}')#cofig faz alteracao na lebel
    entry.delete(0,tk.END)

janela= tk.Tk()
janela.title('ola')
janela.geometry('500x500')
janela.colormapwindows()



lebel = tk.Label(janela,text='tkinter')
lebel.pack(pady=30)
entry= tk.Entry(janela,text='tela')
entry.pack(pady=10)

butao = tk.Button(janela,text='start', command=mostra_nome)
butao.pack(pady=0)
lebel_1 = tk.Label(janela,text='')
lebel_1.pack(pady=30)













janela.mainloop()

