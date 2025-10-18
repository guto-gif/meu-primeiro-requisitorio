import tkinter as tk

def pasta ():
    tela= tk.Tk()
    tela.title('ORGANIZADOR DE ARQUIVOS')
    tela.geometry('500x500')



    lebol= tk.Label(tela,text='PASTA SELECIONADA')
    lebol.pack(pady=30)

    entry= tk.Entry(tela,text='')
    entry.pack(pady=0)

    butao= tk.Button(tela,text='SELECIONAR PASTA',bd=6,bg="#D6C5C0")
    butao.pack(pady=30)
    butao_1= tk.Button(tela,text='  ORGANIZAR PASTA',bd=6,bg="#D6C5C0")
    butao_1.pack(padx=30)
    tela.mainloop()
    
    
pasta()    