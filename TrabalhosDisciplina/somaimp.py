# Desafio 4: 
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Criando uma função para a soma 
def soma(a, b):
# Criando uma variável para a soma dos ímpares
    soma_imp = 0
# Fazendo o loop de a até b, com a condicional de ser ímpar e retornando a soma 
    for x in range(a, b + 1):
        if x % 2 != 0:  
            soma_imp += x
    return soma_imp