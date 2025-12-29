import pandas as pd

# Extração
## Ler arquivo em CSV
df = pd.read_csv('dashboard_credito_Inadimplencia/data/credit_risk_dataset.csv')


print(df.columns)
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


# print(df.head().to_string())
# print(df.info())
# print(df.describe())

x = df['propriedade_casa'].unique()
print(x)