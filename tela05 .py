# grid - frame=sao retangulos detro da janela
#row=sao as linhas linha
#column= sao as colunas
#padx= da espaços na largura
#pady= da espaços na altura
#sticky n=topo - s=embaixo - e= direita -w=esquerda
import tkinter as tk 

janela = tk.Tk()
janela.title('tela')
janela.geometry('500x500')


frame01 = tk.LabelFrame(text='cadastro')
frame01.grid(pady=5)

label_nome= tk.Label(frame01,text='nome')
label_nome.grid(row=0,column=0,padx=5,pady=5)

entray_nome=tk.Entry(frame01,text='')
entray_nome.grid(row=0,column=1,padx=5,pady=5)

label_senha= tk.Label(frame01,text='senha')
label_senha.grid(row=1,column=0,padx=5,pady=5)

entray_senha=tk.Entry(frame01,text='')
entray_senha.grid(row=1,column=1,padx=5,pady=5)


frame02=tk.LabelFrame(text='registro')
frame02.grid(pady=5)

label_registro01= tk.Label(frame02,text='primeiro registro')
label_registro01.grid(row=0,column=0,padx=5,pady=5)


entray_registro01= tk.Entry(frame02)
entray_registro01.grid(row=0,column=1,padx=5,pady=5)

label_registro02= tk.Label(frame02,text='segudo registro')
label_registro02.grid(row=1,column=0,padx=5,pady=5)


entray_registro02= tk.Entry(frame02)
entray_registro02.grid(row=1,column=1,padx=5,pady=5)






janela.mainloop()











