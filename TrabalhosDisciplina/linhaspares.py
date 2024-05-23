# Desafio 5:
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
# Abrindo o arquivo com a função with open no modo read
with open('rosalind_ini5.txt', 'r') as arquivo_input:
# Criando uma variável para todas as linhas do arquivo do input    
    linhas = arquivo_input.readlines()    

# Criando um novo arquivo para o output, no modo escrita
 with open('output.txt', 'w') as arquivo_output:
# Fazendo loop das linhas do índice 1 à linha final, conferindo as linhas pares e escrevendo no arquivo output
    for x in range(1, len(linhas) + 1):  
        if x % 2 == 0:
            arquivo_output.write(linhas[x - 1])  