import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

# Criando função para calcular e plotar a curva do coletor
def curva_coletor(tabela_otu_tsv, step_size=100):
    # Abrindo a tabela de OTUs
    tabela_otu = pd.read_csv(tabela_otu_tsv, sep='\t', index_col=0)
    
    # Inicializando a figura do gráfico
    plt.figure(figsize=(12, 8))
    
    # Definindo um ciclo de cores para as curvas
    colors = cycle(plt.cm.tab20.colors)  # Usando o colormap tab20 para mais variedade de cores
    
    # Loop para cada coluna (amostra) na tabela
    for coluna in tabela_otu.columns:
        # Extraindo a coluna atual
        amostra = tabela_otu[coluna]
        
        # Somando os valores por linha para obter as abundâncias totais de cada OTU
        total_reads = amostra.sum()
        
        # Fazendo a abundância relativa para usar como probabilidade
        probabilidades = amostra / total_reads
        
        # Criando um set vazio para as otus observadas e lista para riqueza e reads acumulados
        otus_observadas = set()
        riqueza_acumulada = []
        reads_acumulados = []
        
        # Amostrando reads proporcionalmente às suas abundâncias até que todas as OTUs sejam observadas e adicionando ao set 
        for i in range(0, int(total_reads), step_size):
            amostras_atuais = np.random.choice(amostra.index, size=step_size, p=probabilidades)
            otus_observadas.update(amostras_atuais)
            reads_acumulados.append(i + step_size)
            riqueza_acumulada.append(len(otus_observadas))
            
            # Quando o número de otus observadas chegar ao total, conta o número de reads acumulados e para
            if len(otus_observadas) == len(amostra.index):
                break
        
        # Plotando a curva do coletor para a amostra atual com uma cor única
        plt.plot(reads_acumulados, riqueza_acumulada, marker='o', linestyle='-', label=f'Amostra {coluna}', color=next(colors))
    
    # Configurando a escala logarítmica para o eixo x (reads acumulados)
    plt.xscale('log')
    plt.xlabel('Número de Reads Acumulados', fontsize=14)
    plt.ylabel('Número de OTUs Acumuladas', fontsize=14)
    plt.title('Curva do Coletor', fontsize=16, fontweight='bold')
    plt.legend()
    plt.grid(True)
    plt.show()

