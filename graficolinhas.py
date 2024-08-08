import pandas as pd
import matplotlib.pyplot as plt

# Carregar o DataFrame
dados_cerveja_excel = 'Exercício Candidatos Estágio.xlsx'
df1 = pd.read_excel(dados_cerveja_excel)

# Remover a coluna indesejada e linhas específicas
df = df1.drop(columns=['Total Volume - Beer - 2015 - Latin America'])
df = df.drop(index=[0, 34, 35])

# Definir empresas de interesse
empresas_interesse = ['Others', 'Anheuser-Busch InBev NV']

# Filtrar os dados para incluir apenas as empresas de interesse
df_filtered = df[df['Unnamed: 1'].isin(empresas_interesse)]

# Selecionar as colunas de anos
anos_colunas = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8']
df_filtered = df_filtered.set_index('Unnamed: 1')[anos_colunas]

# Renomear as colunas para anos
df_filtered.columns = ['2008', '2009', '2010', '2011', '2012', '2013', '2014']

# Somar os volumes de cerveja por empresa e ano
df_summed = df_filtered.groupby(df_filtered.index).sum()

# Plotar o gráfico de linha
plt.figure(figsize=(14, 10))  # Aumentar o tamanho da figura

# Plotar cada empresa
for empresa in empresas_interesse:
    if empresa == 'Others':
        label = 'outros (marcas menores)'
    else:
        label = empresa
    plt.plot(df_summed.columns, df_summed.loc[empresa], label=label, linewidth=6.5)  # Aumentar a largura da linha

plt.xlabel('Ano', fontsize=18)  # Aumentar o tamanho da fonte
plt.ylabel('Volume de Cerveja', fontsize=18)  # Aumentar o tamanho da fonte
plt.title('Crescimento do Volume de Cerveja (Outros e Anheuser-Busch InBev NV) (2008 a 2014)', fontsize=19)  # Aumentar o tamanho da fonte do título
plt.legend(fontsize=16)  # Aumentar o tamanho da fonte da legenda
plt.grid(True, linewidth=6)  # Aumentar a espessura do grid
plt.show()
plt.savefig('figura1.png',dpi=300)
