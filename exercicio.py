#peso / (altura*altura)
#  \n  - e o 'enter'
# \ 'quebra a linha'
#  cont k +cont c 'coloca como comentario'
# cont k +cont u  'desfaz o comentario'


'''
nome = input('qual seu nome??')
peso =float( input('qual seu peso??'))
altura =float(input('qual sua altura??'))
imc= peso/(altura*altura)

print(f'seu nome e {nome}.')
print (f'seu peso {peso}.')
print (f'sua altura e {altura}.')
print (f'seu imc e {imc}')

'''
#exeercicio 2
# quantidades_de_vendas_de_coca = 150<br>
# quantidades_de_vendas_de_pepsi = 130<br>
# preço_unitario_da_coca= 1,50<br>
# preço_unitario_da_pepsi= 1,50<br>
# custo =2.500,00

pepsi =130*1.50
coca=150*1.50
total=pepsi+coca

print(f'faturamento da coca {coca}, faturamento pepsi {pepsi}, lucro da empresa {total}')

'''
metodos com string-
sempre que estivermos lidando com string

string sao listas no python:
-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
 M   A   T   E   U  S     C  A  S  T  R  O
 0   1   2   3   4  5  6  7  8  9  10 11 12 
'''
nome= 'luis augusto'
print(nome[0])
print(nome[-1])
print(nome[6])
print(nome[-3])
print(nome[-3:])
print(len(nome))

#1 .lower() - deixa tudo em minusculo
print(nome.lower())
#2 .upper() - deixa tudo em maiusculo
print(nome.upper())
#3 .title() - deixa tudo em minusculo
print(nome.title())
#4 .strip() - tira o espaços no inicio e fim
print(nome.strip())
#5 .replace() troca uma palavra ex:mateuo po joao. por outra
print (nome.replace('mateos' e 'joao''))
#6 .startswith ('x') verifica se a string começa coma a palavra (letra
print(nome.startswith('mat')
#7 .endswith ('x') verifica se a string começa coma a palavra
print('nome.endswith(0)')
#8 .isdgit() - verifica se a string so tem numeros
numero ='aa'
print(numero.isdgit())
#9 isalfha() - verifica se a string so tem letras
print(nome.isalpha())
#isalnum() -verifica se a string so tem letras ou numeros SEM ESPAÇOS
print (numero.isalnum() )
#count ('x')quntidade de vezes que aparece na string
print (email.count(.))
#find ('x')proucura o texto dentro da string e retorna a posiçao
print (email. find('@'))
      
      
