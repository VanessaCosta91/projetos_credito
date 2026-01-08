import pandas as pd
# Ler arquivo em CSV
df = pd.read_csv('dashboard_credito_Inadimplencia\data\input\credit_risk_dataset.csv')


print('\nNome das colunas: \n', df.columns)

# Troca nome das colunas para facilitar a leitura
df = df.rename(columns={
    'person_age': 'idade',
    'person_income': 'renda',
    'person_home_ownership': 'propriedade_casa',
    'person_emp_length': 'tempo_emprego',
    'loan_intent': 'intencao_emprestimo',
    'loan_grade': 'classificacao',
    'loan_amnt': 'vlr_emprestimo',
    'loan_int_rate': 'tx_juros',
    'loan_status': 'status_emprestimo',
    'loan_percent_income': 'pct_renda_emprestimo',
    'cb_person_default_on_file': 'inadimplencia_arquivada',
    'cb_person_cred_hist_length': 'hist_crendicimanto'
})


print('\nVerifica as primeiras linhas do daframe: \n', df.head().to_string())
print('\nInformações Gerais:')
print(df.info())
print('\nEstatíscas Básicas:\n',df.describe())
print('\nTipos das variáveis:\n',df.dtypes)
valores_coluna_propriedade = df['propriedade_casa'].unique()
print('\nValores unicos da coluna propriedade_casa:', valores_coluna_propriedade)

valores_coluna_intencao = df['intencao_emprestimo'].unique()
print('\nValores unicos da coluna intecao_emprestimo:', valores_coluna_intencao)

print('\nValores duplicados: ', df.duplicated().sum())
duplicados = df[df.duplicated(keep=False)]
print(duplicados.shape)
print(df[df.duplicated()].shape)


print('\nVerificar nulos:\n', df.isnull().sum())