import matplotlib.pyplot as plt
import pandas as pd 
dados_cerveja_excel = 'Exercício Candidatos Estágio.xlsx'
df1 = pd.read_excel(dados_cerveja_excel)
df = df1.drop(columns=[
    'Total Volume - Beer - 2015 - Latin America',
    'Unnamed: 2',
    'Unnamed: 3',
    'Unnamed: 4',
    'Unnamed: 5',
    'Unnamed: 6',
    'Unnamed: 7'
])
#Limpar Df
df = df.drop(index=0)
df = df.drop(index=34)
df = df.drop(index=35)
# Agrupar por empresa e somar os volumes
df_grouped = df.groupby('Unnamed: 1')['Unnamed: 8'].sum()


total_volume = df_grouped.sum()
df_percent = (df_grouped / total_volume) * 100
df_filtered = df_percent[df_percent > 5]

# Criar o gráfico de pizza
plt.figure(figsize=(10, 7))
plt.pie(df_filtered, labels=df_filtered.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Volume - Beer - 2015 - Latin America(Mais de 5%)')
plt.show()