import pandas as pd

# Criando uma função para calcular o TSS
def calcular_otu_tss(tabela_otu):
    # Abrindo a tabela de OTUs
    tabela_otu = pd.read_csv('tabela_otu.tsv', sep='\t', index_col=0)

    # Somando os valores por coluna
    soma_colunas = tabela_otu.sum()

    # Encontrando a coluna com o maior valor de soma
    coluna_maior_soma = soma_colunas.idxmax()

    # Identificando o valor da coluna com o maior valor de soma
    valor_maior_soma = soma_colunas.max()

    # Dividindo o valor de reads de cada OTU pelo total de reads da coluna correspondente
    proporcao_otu = tabela_otu.div(soma_colunas, axis=1)

    # Multiplicando cada valor de reads de OTUs pelo maior valor de soma 
    otu_tss = (proporcao_otu * valor_maior_soma).astype(int)

    # Salvando a tabela em um arquivo TSV 
    otu_tss.to_csv('otu_tss.tsv', sep='\t')

    return otu_tss

