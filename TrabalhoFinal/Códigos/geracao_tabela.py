import numpy as np
import pandas as pd

# Definindo uma função para gerar a tabela:
def gerar_tab():

    # Fazendo arrays para a parte aleatória da tabela 
    np.random.seed(1997)
    tabela = np.random.randint(low=1, high=2900, size=(100, 26)) 

    # Passando para tabela com pandas e adicionando nome das linhas e colunas
    tabela_otu = pd.DataFrame(tabela, index=[f'OTU_{i+1}' for i in range(100)], columns=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # Selecionando subamostras por coluna, para todas as colunas através de um loop
    for coluna in tabela_otu.columns:
        # Calculando o número de linhas que serão selecionadas e transformando em um valor inteiro 
        porcentagem_subamostra = np.random.uniform(0.4, 0.75)
        linhas_subamostra = int(porcentagem_subamostra * len(tabela_otu))
    
        # Selecionando índices de linhas aleatórias dentro da coluna
        linhas_selecionadas = np.random.choice(tabela_otu.index, size=linhas_subamostra, replace=False)
    
        # Definindo os valores das linhas selecionadas como zero
        tabela_otu.loc[linhas_selecionadas, coluna] = 0

    # Salvando a tabela em um arquivo TSV
    tabela_otu.to_csv('tabela_otu.tsv', sep='\t')
 