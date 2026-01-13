import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_tratado = pd.read_csv('dashboard_credito_Inadimplencia\data\output\credit_risk_tratado.csv')

print('\n### Amostra do Dataframe ###\n')
print(df_tratado.head().to_string())

print('\n\n### Taxa Geral de inadimplência: ###\n', round(df_tratado['status_emprestimo'].mean()*100, 2))

# Verifica Inadimplência por variáveis categóricas
status = df_tratado.groupby('nivel_risco')['status_emprestimo'].mean().sort_values()
renda = df_tratado.groupby('faixa_renda')['status_emprestimo'].mean().sort_values()
emprestimo = df_tratado.groupby('faixa_emprestimo')['status_emprestimo'].mean().sort_values()
hist_credito = df_tratado.groupby('faixa_hist_credito')['status_emprestimo'].mean().sort_values()
propriedade_casa = df_tratado.groupby('propriedade_casa')['status_emprestimo'].mean().sort_values()
intencao_emprestimo = df_tratado.groupby('intencao_emprestimo')['status_emprestimo'].mean().sort_values()
pct_renda = df_tratado.groupby('pct_renda_emprestimo')['status_emprestimo'].mean().sort_values()

print('\n### Inadimplência por variáveis categóricas ###')
print('\n')
print(round(status,2))
print('\n')
print(round(renda,2))
print('\n')
print(round(emprestimo,2))
print('\n')
print(round(hist_credito, 2))
print('\n')
print(round(propriedade_casa, 2))
print('\n')
print(round(intencao_emprestimo, 2))

# Verifica percentual do emprestimo sobre por variáveis categóricas
status = df_tratado.groupby('nivel_risco')['pct_renda_emprestimo'].mean().sort_values()
renda = df_tratado.groupby('faixa_renda')['pct_renda_emprestimo'].mean().sort_values()
emprestimo = df_tratado.groupby('faixa_emprestimo')['pct_renda_emprestimo'].mean().sort_values()
hist_credito = df_tratado.groupby('faixa_hist_credito')['pct_renda_emprestimo'].mean().sort_values()
propriedade_casa = df_tratado.groupby('propriedade_casa')['pct_renda_emprestimo'].mean().sort_values()
intencao_emprestimo = df_tratado.groupby('intencao_emprestimo')['pct_renda_emprestimo'].mean().sort_values()
pct_renda = df_tratado.groupby('pct_renda_emprestimo')['pct_renda_emprestimo'].mean().sort_values()

print('\n### Comprometimento da renda por variáveis categóricas ###')
print('\n')
print(round(status,2))
print('\n')
print(round(renda,2))
print('\n')
print(round(emprestimo,2))
print('\n')
print(round(hist_credito, 2))
print('\n')
print(round(propriedade_casa, 2))
print('\n')
print(round(intencao_emprestimo, 2))

comprometimento = df_tratado.groupby('alerta_comprometimento')['status_emprestimo'].mean()
print('\nInadipencia por alto compromentoda renda\n', comprometimento)

# Correlação
corr = df_tratado[['idade', 'renda', 'tempo_emprego', 'vlr_emprestimo', 'tx_juros', 'status_emprestimo', 'pct_renda_emprestimo', 'hist_credito' ]].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.1)
plt.title('Correlação')
plt.show()