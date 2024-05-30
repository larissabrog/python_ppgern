import pandas as pd
import math

# Criando uma função para o índice de Shannon
def calcular_shannon(tabela_otu):
    indices_shannon = {}
    
    # Abrindo a tabela de OTUs
    tabela_otu = pd.read_csv(tabela_otu, sep='\t', index_col=0)
    
    # Calculando o índice de Shannon para cada amostra
    for coluna in tabela_otu.columns:
        amostra = tabela_otu[coluna]
        soma = amostra.sum()
        H = 0
        
        for valor in amostra:
            if valor != 0:  
                proporcao = valor / soma
                H += proporcao * math.log(proporcao)
        
        # Invertendo o sinal 
        indices_shannon[coluna] = -1 * H
    return indices_shannon




