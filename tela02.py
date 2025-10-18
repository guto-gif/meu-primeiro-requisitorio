import tkinter as tk

def calcular_imc():
    altura = float(entry.get())#pega o que esta no entre
    peso = float(entry_e.get())
    resultado = peso/(altura*altura)
    lebel_1.config(text=F'ola, {resultado:.3f}')#cofig faz alteracao na lebel
    # entry.delete(0,tk.END)

janela= tk.Tk()
janela.title('ola')
janela.geometry('500x500')
janela.colormapwindows()



lebel = tk.Label(janela,text='VAUCULADORA DE IMC',font=('Arial',16))
lebel.pack(pady=30)
lebel_L = tk.Label(janela,text='altura')
lebel_L.pack(pady=0)
entry= tk.Entry(janela,text='')
entry.pack(pady=0)


lebel_e = tk.Label(janela,text='peso')
lebel_e.pack(pady=0)
entry_e= tk.Entry(janela,text='')
entry_e.pack(pady=0)


butao = tk.Button(janela,text='resultado', command=calcular_imc)
butao.pack(pady=0)
lebel_1 = tk.Label(janela,text='')
lebel_1.pack(pady=30)


tk.mainloop()