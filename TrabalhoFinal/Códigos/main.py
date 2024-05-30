# Importando as bibliotecas e funções usadas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro, levene, f_oneway
from geracao_tabela import gerar_tab
from rarefacao import otu_rarefacao
from tss import calcular_otu_tss
from coletor2 import curva_coletor
from shannon import calcular_shannon
from scipy.spatial.distance import pdist
from scipy.stats import ttest_rel

def main():
    # Gerando a tabela
    tabela_otu_original = gerar_tab()

    # Abrindo a tabela criada
    tabela_otu = pd.read_csv('tabela_otu.tsv', sep='\t', index_col=0)

    # Usando a função para gerar a tabela rarefeita
    tabela_otu_rarefeita = otu_rarefacao('tabela_otu.tsv')

    # Usando a função para gerar a tabela TSS
    tabela_otu_tss = calcular_otu_tss('tabela_otu.tsv')

    # Abrindo as tabelas
    otu_tss = pd.read_csv('otu_tss.tsv', sep='\t', index_col=0)
    otu_rarefeita = pd.read_csv('tabela_otu_rarefeita.tsv', sep='\t', index_col=0)

    # Calculando a média e o desvio padrão para cada tabela
    media_otu = tabela_otu.mean()
    desvio_padrao_otu = tabela_otu.std()

    media_rarefeita = otu_rarefeita.mean()
    desvio_padrao_rarefeita = otu_rarefeita.std()

    media_otu_tss = otu_tss.mean()
    desvio_padrao_otu_tss = otu_tss.std()

    # Criando um dataframe para armazenar os resultados
    tabelamedia = pd.DataFrame({
        'Média OTU': media_otu,
        'Desvio Padrão OTU': desvio_padrao_otu,
        'Média Rarefeita': media_rarefeita,
        'Desvio Padrão Rarefeita': desvio_padrao_rarefeita,
        'Média OTU TSS': media_otu_tss,
        'Desvio Padrão OTU TSS': desvio_padrao_otu_tss
    })

    # Salvando os resultados em um arquivo TSV
    tabelamedia.to_csv('tabelamedia_reads.tsv', sep='\t')

    # Plotando gráfico boxplot de comparação
    soma_otu = tabela_otu.sum()
    soma_rarefeita = otu_rarefeita.sum()
    soma_tss = otu_tss.sum()

    # Criando um dataframe para os dados do boxplot
    data = pd.DataFrame({
        'Tratamento': ['Original'] * len(soma_otu) + ['Rarefeito'] * len(soma_rarefeita) + ['TSS'] * len(soma_tss),
        'Reads': list(soma_otu) + list(soma_rarefeita) + list(soma_tss)
    })

    # Plotando o boxplot
    plt.figure(figsize=(10, 8))
    sns.boxplot(x='Tratamento', y='Reads', data=data)
    plt.title('Boxplot: reads por tratamento')
    plt.xlabel('Tratamento')
    plt.ylabel('Reads')
    plt.savefig('boxplot_reads.png')  # Salva o plot em um arquivo
    plt.close()

    # Chamando função para a curva do coletor para a tabela original
    curva_original = curva_coletor('tabela_otu.tsv', step_size=10)

    # Chamando função para a curva do coletor para a tabela rarefeita
    curva_rarefeita = curva_coletor('tabela_otu_rarefeita.tsv', step_size=10)

    # Chamando função para a curva do coletor para a tabela TSS
    curva_tss = curva_coletor('otu_tss.tsv', step_size=10)

    # Calculando o índice de Shannon para a tabela original
    shannon_original = calcular_shannon('tabela_otu.tsv')

    # Calculando o índice de Shannon para a tabela rarefeita
    shannon_rarefeita = calcular_shannon('tabela_otu_rarefeita.tsv')

    # Calculando o índice de Shannon para a tabela TSS
    shannon_tss = calcular_shannon('otu_tss.tsv')

    # Criando um DataFrame com os índices de Shannon para cada amostra nos três tratamentos
    df_shannon = pd.DataFrame({
        'Amostra': list(shannon_original.keys()),
        'Original': list(shannon_original.values()),
        'Rarefeito': list(shannon_rarefeita.values()),
        'TSS': list(shannon_tss.values())
    })

    # Definindo a coluna amostra como índice
    df_shannon.set_index('Amostra', inplace=True)

    # Salvando a tabela
    df_shannon.to_csv('indices_shannon.tsv', sep='\t')

    # Verificando a normalidade dos dados com o teste de Shapiro-Wilk
    shapiro_resultados = {}
    for coluna in df_shannon.columns:
        shapiro_resultados[coluna] = shapiro(df_shannon[coluna])

    print('Resultados do teste de Shapiro-Wilk:')
    for coluna, resultado in shapiro_resultados.items():
        print(f'{coluna}: W={resultado.statistic}, p-value={resultado.pvalue}')

    # Verificando a homogeneidade das variâncias com o teste Levene
    teste_levene = levene(df_shannon['Original'], df_shannon['Rarefeito'], df_shannon['TSS'])
    print(f'Resultado do teste de Levene: W={teste_levene.statistic}, p-value={teste_levene.pvalue}')

    # Verificando se há diferença significativa entre os índices de Shannon (p<0.05) com o teste ANOVA
    anova_shannon = f_oneway(
        df_shannon['Original'],
        df_shannon['Rarefeito'],
        df_shannon['TSS']
    )

    print('Resultado ANOVA:', anova_shannon)
    
    # Verificando a distância de Bray-Curtis entre as amostras da tabela original e rarefeita
    def braycurtis(tabelaotu1, tabelaotu2):
        return pdist(np.array([tabelaotu1, tabelaotu2]), metric='braycurtis')[0]

    # Extraindo os nomes das amostras
    amostras = tabela_otu.columns[1:]

    # Calculando a dissimilaridade de Bray-Curtis entre original e rarefeita
    bray_curtis_original_vs_rarefeita = {
        amostra: braycurtis(tabela_otu[amostra].values, tabela_otu_rarefeita[amostra].values)
        for amostra in amostras
    }

    # Calculando a dissimilaridade de Bray-Curtis entre original e normalizada
    bray_curtis_original_vs_normalizada = {
        amostra: braycurtis(tabela_otu[amostra].values, otu_tss[amostra].values)
        for amostra in amostras
    }

    # Criando um DataFrame com os resultados das dissimilaridades
    df_resultados = pd.DataFrame({
        'Amostra': amostras,
        'Dissimilaridade_Rarefeita': list(bray_curtis_original_vs_rarefeita.values()),
        'Dissimilaridade_Normalizada': list(bray_curtis_original_vs_normalizada.values())
    })

    # Realizndo o teste t para comparar as dissimilaridades
    t_statistic, p_values = ttest_rel(df_resultados['Dissimilaridade_Rarefeita'], df_resultados['Dissimilaridade_Normalizada'])

    # Exibindo os resultados do teste t
    print('Resultado do teste t:')
    print('Estatística t:', t_statistic)
    print('Valor p:', p_values)

    # Analisando qual dissimilaridade é maior
    dissimilaridade_rarefeita = df_resultados['Dissimilaridade_Rarefeita'].mean()
    dissimilaridade_normalizada = df_resultados['Dissimilaridade_Normalizada'].mean()

    if dissimilaridade_rarefeita > dissimilaridade_normalizada:
        print('A dissimilaridade original vs rarefeita é maior.')
    elif dissimilaridade_rarefeita < dissimilaridade_normalizada:
        print('A dissimilaridade original vs normalizada é maior.')
    else:
        print('As dissimilaridades são iguais.')

    # Printando uma mensagem final
    print('Trabalho final da disciplina de Python para Biocientistas feito por Larissa Broggio Raymundo')
if __name__ == '__main__':
    main()
