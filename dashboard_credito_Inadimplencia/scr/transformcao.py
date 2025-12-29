import pandas as pd
import numpy as np

## Ler arquivo em CSV
df = pd.read_csv('dashboard_credito_Inadimplencia/data/credit_risk_dataset.csv')

# Traduzir nome das colunas para português
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
    'cb_person_cred_hist_length': 'hist_credito'
})

# Criar coluna com classicação de nível de risco

mapa_risco = {
    'A': 'Risco Muito Baixo',
    'B': 'Risco Baixo',
    'C': 'Risco Médio-Baixo',
    'D': 'Risco Médio',
    'E': 'Risco Médio-Alto',
    'F': 'Risco Alto',
    'G': 'Risco Muito Alto'
}

df['nivel_risco'] = df['classificacao'].map(mapa_risco)

# Tratamento de valores extremos ou implausiveis
## Transfomar idades menores que 18 e maiores 80 em valores nulos (18-80 são idades comumentes utilizadas em instituições financerias)
df.loc[
    (df['idade'] < 18) | (df['idade'] > 80), 'idade'
    ] = np.nan

## Transformar tempo de trabalho em nultos. Foi adotado como cirterio tempo inferior a 0, e idade-14 (visto que a legislação brasileria permite o primerio emprego 14 anos, embora seja um situação rara ainda é possíve) 
df.loc[
    (df['tempo_emprego'] < 0) |
    (df['tempo_emprego'] >= (df['idade'] - 14)),
    'tempo_emprego'
] = np.nan


# Cria coluna com baixa de de renda
df['faixa_renda'] = pd.qcut(
    df['renda'],
    q=5,
    labels=[
        'Muito Baixa',
        'Baixa',
        'Média',
        'Alta',
        'Muito Alta'
    ]
)

# Cria columa com faixa de emprestimo
df['faixa_emprestimo'] = pd.cut(
    df['vlr_emprestimo'],
    bins=[0, 3000, 7000, 15000, 30000, df['vlr_emprestimo'].max()],
    labels=['Muito Baixo', 'Baixo', 'Médio', 'Alto', 'Muito Alto']
)

# Cria coluna de aletar quando o compromentimento da renda esta alto
df['alerta_comprometimento'] = df['pct_renda_emprestimo'] >= 0.4

# Cria coluna de historico de credito 
df['faixa_hist_credito'] = pd.cut(
    df['hist_credito'],
    bins=[0, 2, 5, 10, 20, 50],
    labels=['Muito Curto', 'Curto', 'Médio', 'Longo','Muito Longo']
)

# Traduz infromações nas colunas proprieade da casa e inadiplencia arquivada
mapa_casa = {
    'RENT': 'Alugada',
    'OWN': 'Propria',
    'MORTGAGE': 'Financiada',
    'OTHER': 'Outros'
}

df['propriedade_casa'] = df['propriedade_casa'].map(mapa_casa)

df['inadimplencia_arquivada'] = df['inadimplencia_arquivada'].map({'Y': 'Sim', 'N': 'Não'})

print(df.head().to_string())

print(df.describe())

