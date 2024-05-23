# Desafio 6:
# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

# Criando uma função para contar as palavras da string s 
def contar_palavras(s):

# Transformando a string em uma lista de palavras usando split para separar as palavras
    lista = s.split()

    # Criando um dicionário para contar as palavras
    dicionario = {}

    # Contando as palavras com condicional
    for palavra in lista:
        if palavra in dicionario:
            dicionario[palavra] += 1    # Se a palavra já estiver no dicionário, conta mais uma vez
        else:
            dicionario[palavra] = 1 # Se não, adiciona e conta uma vez
   return dicionario
    
    # Visualizando o resultado
    resultado = contar_palavras(s)  
for palavra, contagem in resultado.items():  
    print(f"{palavra} {contagem}")