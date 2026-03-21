# Análise de Eficiência de Cobrança

Este projeto tem como objetivo analisar a eficiência de cobrança, buscando identificar padrões de comportamento de pagamento e traçar o perfil dos clientes com maior risco de inadimplência.

## 1. Coleta de Dados

- **Origem**: Dataset público do Google BigQuery
- **Acesso**: BigQuery (via SQL)
- **Formato**: Dados estruturados em tabela relacional
- **Tipo de dado**: Informações financeiras anonimizadas relacionadas a faturamento, pagamentos e histórico de atraso dos clientes

## 2. Preparação e métricas base

A etapa de pré-processamento foi realizada utilizando SQL no BigQuery, seguindo uma arquitetura em camadas (dados brutos → dados limpos → métricas → dataset final).

### 2.1. Limpeza
Nesta etapa foi criada uma view contendo os dados tratados e padronizados. As principais ações realizadas foram:
- Padronização e renomeação das colunas
- Seleção apenas das variáveis relevantes para a análise
- Tratamento de inconsistências, incluindo:
    -Limite de crédito válido (não nulo e maior que zero)
    - Idade entre 18 e 100 anos
    - Validação de categorias de gênero (valores 1 e 2)
    - Valores de faturas e pagamentos positivos
    - Validação do histórico de atraso (valores entre -2 e 8)

### 2.2. Métricas
Foram desenvolvidas métricas financeiras e comportamentais para avaliar a eficiência de cobrança.

- Métricas de Pagamento
    - Valor total faturado nos últimos 6 meses
    - Valor total pago no período
    - Percentual de pagamento
    - Saldo devedor residual
    - Nível de eficiência de pagamento

- Métricas de Atraso
    - Indicador de atraso recente
    - Total de meses em atraso
    - Maior atraso registrado
    - Identificação de clientes pontuais

### 2.3. daset_final
Foi criada uma view consolidada unindo:
- Foi criada uma view consolidada unindo:
- Dados limpos dos clientes
- Métricas comportamentais de atraso

Essa base final foi utilizada para as etapas posteriores de análise exploratória e visualização.

### Arquitetura do Pipeline de Dados
Cada etapa do processo resultou na criação de uma view no BigQuery, seguindo a seguinte estrutura:
- vw_credit_card_clean: dados tratados
- vw_metricas_pagamento: métricas financeiras
- vw_metricas_atraso: métricas comportamentais
- vw_dataset_final: base consolidada para análise

## 3 - Análise Exploratória de Dados (EDA)

Foi realizada uma análise exploratória dos dados a partir do dataset final, com os seguintes principais achados:

-  Distribuição do limite de crédito: a maior parte dos clientes possui limite inferior a 100 mil, indicando concentração em faixas de menor exposição ao risco;
- Perfil demográfico dos clientes: 
    - base predominantemente feminina;
    - com idade inferior a 45 anos;
    - com idade inferior a 45 anos;
    - com nível de escolaridade superior;
- Distribuição do percentual de pagamento: indica predominância de pagamentos parciais, com presença de casos em que há quitação de dívidas acumuladas;
- Relação entre faturado e pago: : reforça o padrão de pagamento parcial e o acúmulo de dívida ao longo do tempo;
- Distribuição de atraso recente: a maior parte dos clientes não apresenta atraso no período mais recente, embora exista uma parcela relevante com atraso;
- Distribuição do total de meses em atraso: confirma que a maioria dos clientes mantém seus pagamentos em dia, porém frequentemente realiza pagamentos parciais;
- Relação entre Atraso e Eficiência de Pagamento: quanto maior o número de meses em atraso, menor tende a ser o percentual de pagamento;
- Correlação entre variáveis financeiras: quanto maior o número de meses em atraso, menor tende a ser o percentual de pagamento;

**Principal Conclusão**: 
As estratégias de cobrança devem considerar não apenas clientes em atraso, mas também aqueles que realizam pagamentos mínimos recorrentes, buscando reduzir o risco de inadimplência futura.