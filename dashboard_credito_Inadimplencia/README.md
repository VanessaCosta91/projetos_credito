# Credito e inadimplencia

Este projeto visa cria um Dashboard interetivo que cubra os três pilares do crédito: perfil do cliente, características do emprestimo e histórico de crédito, perminto assim, um analise completa de risco e inadiplencia.

---

## 1. Coleta de dados
- **Origem**: plataforma [Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)
- **Acesso**: arquivo `.csv`
- **Tipo de Dados**: dados tabulares com dados financeiros

---

## 2. ETL (Extração, Transformação e Carga)

### 2.1 - Extração (E)

O dataset [Credit Risk Dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset), em formato `.csv`, foi baixado em um repositório local.
A extração foi feito com o mando `pd.read_csv()` que ao mesmo tempo que lê o arquivo `.csv` o transforma em dataframe.

```
df = pd.read_csv('dashboard_credito_Inadimplencia/data/credit_risk_dataset.csv')
```

### 2.2 - Transformação
- Criação da coluna grau de risco
- Tratamento de valores extremo ou implausiveis 
- 

### 2.3 - Carga

- Foi salvo o arquivo com dados transformatos em formato `.csv`

---

## 3 - Análise Exploratória de Dados (EDA)

Nesta etapa, foi realizada uma análise exploratória sobre o dataset tratado, com foco na identificação de padrões relacionados à inadimplência e ao risco de crédito.

**Principais insiths:**
- A taxa geral de inadiplência da base de dados é relativamente baixa, em torno de 22%, indicando um portfólio predominantemente adimplente.
- Ao analisar a inadimplência por categorias, se observa que as maiores taxas estão associadas a:
    - níveis de risco mais elevados,
    - faixas de renda mais baixas,
    - valores de empréstimo mais altos,
    - clientes que moram em imóveis alugados,
    - empréstimos com finalidade de quitação de dívidas.
- Em relação ao histórico de crédito, as diferenças de inadimplência entre as faixas são menos expressivas. Ainda assim, os históricos mais longos apresentam levemente maiores taxas, o que pode indicar exposição acumulada ao crédito ao longo do tempo.
- O maior comprometimento da renda está concentrado em operações de:
    - risco elevado,
    - baixa renda,
    - alto valor de empréstimo,
    - histórico de crédito curto.
- Clientes que comprometem mais de 40% da renda com o empréstimo apresentam maior probabilidade de inadimplência, reforçando o comprometimento da renda como um importante indicador de risco.

**Correlação entre variáveis numéricas:** <p>
A análise de correlação entre as variáveis numéricas indicou relações fracas na maior parte dos casos. As correlações mais relevantes observadas foram entre idade e histórico de crédito, e entre renda e percentual de comprometimento da renda, o que é consistente com o contexto de crédito.

---

## 4 - Dashboard



