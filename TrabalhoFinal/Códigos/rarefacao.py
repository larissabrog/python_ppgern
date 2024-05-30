import pandas as pd
import numpy as np

# Definindo uma função para calcular a rarefação
def otu_rarefacao(tabela_otu):
    # Abrindo a tabela de OTUs
    tabela_otu = pd.read_csv(tabela_otu, sep='\t', index_col=0)

    # Somando os valores por coluna
    soma_colunas = tabela_otu.sum()

    # Encontrando a soma mínima entre as colunas 
    soma_minima = soma_colunas.min()

    # Dividindo o valor de reads de cada OTU pelo total de reads da coluna 
    proporcao_otu = tabela_otu.div(soma_colunas, axis=1)

    # Criando uma tabela para armazenar os dados rarefeitos
    otu_rarefacao = pd.DataFrame(index=tabela_otu.index, columns=tabela_otu.columns)

    # Fazendo um loop para cada coluna
    for coluna in tabela_otu.columns:
        proporcoes = proporcao_otu[coluna]

        # Começando uma nova coluna (rarefeita) com zeros
        coluna_rarefeita = np.zeros(len(proporcoes))

        # Amostrando até que a soma atual chegue na soma mínima
        soma_atual = 0
        while soma_atual < soma_minima:
            # Escolhendo uma OTU aleatoriamente com base nas proporções
            otu_escolhida = np.random.choice(proporcoes.index, p=proporcoes)
            
            # Adicionando a OTU escolhida na coluna rarefeita (soma +1 quando é escolhida)
            coluna_rarefeita[proporcoes.index.get_loc(otu_escolhida)] += 1
            
            # Atualizando a soma atual (controla o loop até a soma mínima)
            soma_atual += 1

        # Atribuindo a coluna rarefeita à tabela de rarefação
        otu_rarefacao[coluna] = coluna_rarefeita 

    # Convertendo os valores da tabela para inteiros
    otu_rarefacao = otu_rarefacao.astype(int)
    
    # Salvando a tabela rarefeita em um arquivo TSV
    otu_rarefacao.to_csv('tabela_otu_rarefeita.tsv', sep='\t')

    # Retornando a tabela rarefeita
    return otu_rarefacao


