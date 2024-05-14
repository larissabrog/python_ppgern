# Definindo os dados em sets entrados em aula 
A1 = {2, 3, 4, 5, 6}
A2 = {1, 2, 4, 5}
A3 = {0, 1, 5, 7, 2, 4} 

# Definindo o que tem em comum nos três conjuntos
regiao_7 = A1.intersection(A2, A3)

# Definindo o que tem em comum nos dois conjuntos
regiao_2 = A1.intersection(A2) - regiao_7
regiao_5 = A2.intersection(A3) - regiao_7
regiao_6 = A1.intersection(A3) - regiao_7

# Definindo o que tem somente em um conjunto
regiao_1 = A1 - regiao_2 - regiao_6 - regiao_7
regiao_3 = A2 - regiao_2 - regiao_5 - regiao_7
regiao_4 = A3 - regiao_5 - regiao_6 - regiao_7

# Mostrando os resultados
print('Oi, temos os seguintes resultados:')
print('Região 1 =', regiao_1, '\nRegião 2 =', regiao_2, '\nRegião 3 =',
       regiao_3, '\nRegião 4 =', regiao_4, '\nRegião 5 =', regiao_5, 
       '\nRegião 6 =', regiao_6, '\nRegião 7 =', regiao_7)
