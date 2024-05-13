#Atividade em grupo
#Alunos: Gustavo Fernando Mastrocollo Gea - RA 623201135
#        Guilherme Paiva Flora            - RA 623200498

import pandas as pd

# URL do arquivo CSV no GitHub
url = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"

# Importando os dados e definindo a primeira coluna como índice
df = pd.read_csv(url, index_col=0)

# Groupby: Agrupando por cilindro (cyl) e transmissão (am), trazendo os valores médios e ordenando por ordem descrescente de peso (wt) médio
grouped_df = df.groupby(['cyl', 'am']).mean().sort_values(by='wt', ascending=False)
print("Groupby:")
print(grouped_df)

# Pivot Table: Criando uma tabela pivot com tipos de motores (vs) como linhas, transmissão (am) como colunas, usando a mediana (median) como função de agregração (aggfun) do valor de cavalos de potência (hp) e consumo (mpg), trazendo os subtotais (margins)
pivot_table = pd.pivot_table(df, index='vs', columns='am', values=['hp', 'mpg'], aggfunc='median', margins=True)
print("\nPivot Table:")
print(pivot_table)

# Crosstab: Criando uma tabela de frequência (count) dos números de cilindros (cyl) como linhas, transmissão (am) como colunas, trazendo os subtotais (margins)
cross_tab = pd.crosstab(index=df['cyl'], columns=df['am'], margins=True)
print("\nCrosstab:")
print(cross_tab)
