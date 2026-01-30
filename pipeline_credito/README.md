# Pipeline de Dados de Fraude em Cartão de Crédito

Este projeto cria um pipeline completo de dados, desde a coleta até a carga final em banco de dados SQL, utilizando um dataset público de transações de cartão de crédito com foco em fraude.

O objetivo principal é demonstrar boas práticas de engenharia e análise de dados, como validação de dados, geração de métricas analíticas e persistência dos resultados.

---

## Visão Geral do Pipeline

O pipeline foi organizado em etapas simples e bem definidas:

Coleta dos dados -> Dados brutos (arquivo CSV) -> Dados preparados e validados -> Análises e métricas -> Armazenamento no banco de dados

---

## 1. Coleta de Dados

- **Origem**: Plataforma Kaggle  
- **Acesso**: API oficial do Kaggle  
- **Formato**: Arquivo CSV  
- **Tipo de dado**: Transações financeiras anonimizadas para detecção de fraude

Nesta etapa, os dados são apenas extraídos e armazenados, sem qualquer modificação.

## 2. ETL (Extração, Transformação e Carga)

### 2.1 Extração

A extração é realizada por meio da Kaggle API, que permite automatizar o download do dataset.

Principais características:
- Autenticação via token do Kaggle
- Download automático do CSV
- Armazenamento local na pasta `data/raw`
- Nenhuma alteração nos dados originais

---

### 2.2 Transformação 

A transformação ocorre na função `bruto_para_preparacao`, responsável por garantir a qualidade e a consistência dos dados.

Nesta etapa são realizadas as seguintes ações:

- Validação se o DataFrame não está vazio
- Validação do schema (verificação das colunas essenciais `Amount` e `Class`)
- Validação de regras técnicas:
  - `Class` deve conter apenas valores 0 ou 1
  - `Amount` não pode conter valores negativos
- Padronização dos tipos de dados
- Criação de colunas técnicas:
  - `amount_log`: transformação logarítmica do valor da transação
  - `is_fraud`: indicador booleano de fraude

Aqui não altera o significado dos dados, apenas garante que eles respeitam um contrato mínimo de qualidade.

---

### 2.3 Análises

Na etapa, os dados preparados são agregados e transformados em informação analítica.

Foi criada uma análise segmentada por faixa de valor da transação, permitindo observar o comportamento da fraude em diferentes intervalos.

As principais métricas geradas são:

- `qtde_transacoes`: quantidade de transações por faixa de valor
- `valor_total_transacoes`: soma dos valores das transações
- `total_fraudes`: número de transações fraudulentas
- `percentual_fraude`: proporção de fraudes dentro de cada faixa

Essa etapa representa o resultado final do pipeline, pronto para consumo analítico ou visualização.

---

### 2.4 Carga

Após a geração das análise, os dados são persistidos em um banco de dados SQLite.

Características da carga:
- Uso de banco SQL leve e local
- Criação automática do banco e da tabela
- Substituição da tabela a cada execução (pipeline reexecutável)

---

## 3. Ferramentas Utilizadas

- **Python:** linguagem principal do pipeline  
- **Pandas / NumPy:** manipulação e análise de dados  
- **Kaggle API:** ingestão automatizada dos dados  
- **SQLite:** persistência final dos dados  
- **VS Code:** – desenvolvimento  

---

## 4. Como Usar

### Pré-requisitos
- Python 3.9+
- Conta no Kaggle com token de API configurado

### Passo a passo

1. Clone o repositório:
```
git clone <url-do-repositorio>
cd pipeline_credito
```

2. Crie e ative um ambiente virtual:
```
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Configure o token da Kaggle:
- Crie o arquivo kaggle.json
- Posicione em ~/.kaggle/ (Linux/Mac) ou C:\Users\<usuario>\.kaggle\ (Windows)

5. Execute o pipeline:
```
python src/main.py
```

6. Verifique os resultados:
- Logs gerados em pipeline.log
- Banco SQLite criado em data/database/
- Tabela final com os dados analíticos

---

## 5. Decisões Técnicas e Boas Práticas
- Logging centralizado na função principal
- Validações explícitas para evitar propagação de dados inválidos
- Uso de nomes de funções e variáveis descritivos
- Pipeline reexecutável e independente de notebook
- Dados e logs excluídos do versionamento (.gitignore)

---

## Autor
Vanessa Costa

Projeto desenvolvido para fins de estudo e portfólio, com foco em pipeline de dados, análise de dados e risco de crédito.
