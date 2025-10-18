# import tkinter as tk
# from tkinter import messagebox





# # def cadastro():
# #     altura = float(entry.get())#pega o que esta no entre
# #     peso = float(entry_e.get())
# #     resultado = peso/(altura*altura)
# #     lebel_1.config(text=F'ola, {resultado:.3f}')#cofig faz alteracao na lebel
# #     # entry.delete(0,tk.END)
# # DICIONRIO PARA ARMAZENAR OS CADATROS
# dados = {'admin': '1234'}

# #FUNÇÕES
# def abrir_login():
#     def fazer_usuario():
#         usuario = entry.get()
#         senha = entry_e.get()
        

#         if usuario in dados and dados [usuario] == senha:
#                lebel_2.config (text='login realizado com sucesso')
#         else:
#              lebel_2.config (text='usuario ou senha incorreta')  
#         def castrastra():
                      
#          janela.destroy()

     
    
    
    
#     janela = tk.Tk()
#     janela.title('ola')
#     janela.geometry('500x500')
#     janela.colormapwindows()



#     lebel = tk.Label(janela,text='ACESSO AO SISTEMA',font=('Arial',16), bd=6  )
#     lebel.pack(pady=30) 
#     entry_usu = tk.Label(janela,text='USUARIOS')
#     entry_usu.pack(pady=0)
#     entry= tk.Entry(janela,text='')
#     entry.pack(pady=0)


#     entry_sen= tk.Label(janela,text='SENHA')
#     entry_sen.pack(pady=0)
#     entry_e= tk.Entry(janela,text='')
#     entry_e.pack(pady=0)


#     butao = tk.Button(janela,text='LOGIN', command=fazer_usuario,bd=6)
#     butao.pack(pady=30)
#     butao_b = tk.Button(janela,text='CADASTRA', command=abrir_login,bd=6)
#     butao_b.pack(pady=0)
#     lebel_1 = tk.Label(janela,text='')
#     lebel_1.pack(pady=30)
#     lebel_2 = tk.Label(janela,text='')
#     lebel_2.pack(pady=30)


#     tk.mainloop()

# abrir_login()  


# def abrir_tela_cadastro():
#      janela_cadasto=tk.Tk()
#      janela_cadasto.title('janela_cadasto')
#      janela_cadasto.geometry('500x500')

#      def cadastro_usuario():
#           novo_cadastro=entry_usu.get()
#           novo_senha=  entry_sen.get()

#           if novo_cadastro in dados:
#               messagebox.showerror('erro' , 'usuario existente')

#           else:
#               dados[novo_cadastro]    




          
     
    

    #  lebel = tk.Label(janela,text='ACESSO AO SISTEMA',font=('Arial',16), bd=6  )
    #  lebel.pack(pady=30) 
    #  entry_usu = tk.Label(janela,text='USUARIOS')
    #  entry_usu.pack(pady=0)
    #  entry= tk.Entry(janela,text='')
    #  entry.pack(pady=0)


    #  entry_sen= tk.Label(janela,text='SENHA')
    #  entry_sen.pack(pady=0)
    #  entry_e= tk.Entry(janela,text='')
    #  entry_e.pack(pady=0)


    #  butao = tk.Button(janela,text='LOGIN', command=fazer_usuario,bd=6)
    #  butao.pack(pady=30)
    #  butao_b = tk.Button(janela,text='CADASTRA', command=abrir_login,bd=6)
    #  butao_b.pack(pady=0)
    #  lebel_1 = tk.Label(janela,text='')
    #  lebel_1.pack(pady=30)
    #  lebel_2 = tk.Label(janela,text='')
    #  lebel_2.pack(pady=30)

import tkinter as tk
from tkinter import messagebox


#Dicionarios para armazenar os cadastros
dados = {'admin': '123'}

#Funcoes

def abrir_tela_cadastro():
    janela_cadastro = tk.Tk()
    janela_cadastro.title('Cadastro de usuário')
    janela_cadastro.geometry('300x300')

    def cadastrar_usuario():
        novo_usuario = entry_usu.get()
        nova_senha = entry_sen.get()

        if novo_usuario in dados:
            messagebox.showerror('Erro','Usuário Já existe!')
        
        else:
            dados[novo_usuario] = nova_senha
            messagebox.showinfo('Sucesso','Cadastro Realizado')
            janela_cadastro.destroy()
            abrir_login()




    label_ini = tk.Label(janela_cadastro,text='Cadastro de usuário',font=('Arial',18))
    label_ini.pack(pady=5)

    label_usu = tk.Label(janela_cadastro,text='Usuario')
    label_usu.pack(pady=5)
    entry_usu = tk.Entry(janela_cadastro)
    entry_usu.pack(pady=5)

    label_sen = tk.Label(janela_cadastro,text='Senha')
    label_sen.pack(pady=5)
    entry_sen = tk.Entry(janela_cadastro)
    entry_sen.pack(pady=5)

    botao_cad = tk.Button(janela_cadastro,text='Cadastrar',command=cadastrar_usuario)
    botao_cad.pack(pady=10)

    #botao_voltar = tk.Button(janela_cadastro,text='voltar')
    #botao_voltar.pack(pady=10)


    label_vazia = tk.Label(janela_cadastro,text='xxxxx')
    label_vazia.pack(pady=1)
    janela_cadastro.mainloop()



abrir_tela_cadastro()



def abrir_login():

    def fazer_login():
        usuario = entry_usu.get()
        senha = entry_sen.get()


        if usuario in dados and dados[usuario] == senha:
            label_vazia.config(text='Login Realizado com sucesso!')
        
        else:
            label_vazia.config(text='Usuário ou senha incorretos.')    
    
    def cadastrar():
        janela.destroy()
        abrir_tela_cadastro()

    janela = tk.Tk()
    janela.geometry('300x300')
    janela.title('Tela de Login')

    label_ini = tk.Label(janela,text='Acesso ao Sistema',font=('Arial',18))
    label_ini.pack(pady=5)

    label_usu = tk.Label(janela,text='Usuario')
    label_usu.pack(pady=5)
    entry_usu = tk.Entry(janela)
    entry_usu.pack(pady=5)

    label_sen = tk.Label(janela,text='Senha')
    label_sen.pack(pady=5)
    entry_sen = tk.Entry(janela,show='*')
    entry_sen.pack(pady=5)

    botao_login = tk.Button(janela,text='Login',command=fazer_login)
    botao_login.pack(pady=10)

    botao_cad = tk.Button(janela,text='Cadastrar',command=cadastrar)
    botao_cad.pack(pady=10)

    label_vazia = tk.Label(janela,text='xxxxx')
    label_vazia.pack(pady=1)
    janela.mainloop()


abrir_login()







abrir_login()    
    
    
    

