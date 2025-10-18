
'''
CSV - ARQUIVO DE VALORES SEPARADO POR VIRGULAR -CADA LINHA E UM ARQUIVO DE DADOS SEPARADO POR VIRGULAR
O que é o formato CSC?
O formato CSC é otimizado para fatiamento rápido de colunas e operações aritméticas eficientes. É semelhante ao CSR, mas comprime a matriz armazenando apenas os elementos diferentes de zero e os índices de coluna correspondentes. A estrutura é dividida em três matrizes unidimensionais:

Dados : Armazena os valores diferentes de zero.
Índices : Armazena os índices de linha dos elementos na matriz de dados.
Indptr : armazena os ponteiros de índice no início de cada coluna na matriz de dados.


'''
from scipy.sparse import csc_matrix
m = np.array([
    [0, 0, 1],
    [4, 0, 0],
    [0, 0, 3]
])

csc = csc_matrix(m)
print(csc)

print("\nData:", csc.data)
print("Indices:", csc.indices)
print("Indptr:", csc.indptr)