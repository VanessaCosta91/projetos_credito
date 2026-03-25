-- Cria View com métricas com valores dos pagamentos
CREATE OR REPLACE VIEW analise_cobranca.vw_metricas_pagamento AS
WITH totais AS (
SELECT
  id_cliente,
  limite_credito,

  COALESCE(valor_emitido_1,0) + COALESCE(valor_emitido_2,0) +
  COALESCE(valor_emitido_3,0) + COALESCE(valor_emitido_4,0) +
  COALESCE(valor_emitido_5,0) + COALESCE(valor_emitido_6,0) AS valor_total_faturado,

  COALESCE(valor_pago_1,0) + COALESCE(valor_pago_2,0) +
  COALESCE(valor_pago_3,0) + COALESCE(valor_pago_4,0) +
  COALESCE(valor_pago_5,0) + COALESCE(valor_pago_6,0) AS valor_total_pago

FROM analise_cobranca.vw_credit_card_clean
)
SELECT 
  id_cliente,
  limite_credito,
  valor_total_faturado,
  valor_total_pago,  
  ROUND(SAFE_DIVIDE(valor_total_pago, valor_total_faturado)* 100,2) AS percentual_pago
FROM totais
ORDER BY percentual_pago DESC;

-- Cria View com métricas de meses atrasados
CREATE OR REPLACE VIEW analise_cobranca.vw_metricas_atraso AS
SELECT
  id_cliente,

  CASE 
    WHEN atraso_mes_recente > 0 THEN 1
    ELSE 0
  END AS atraso_recente,

  (
    CASE WHEN atraso_mes_recente > 0 THEN 1 ELSE 0 END +
    CASE WHEN atraso_mes_2 > 0 THEN 1 ELSE 0 END +
    CASE WHEN atraso_mes_3 > 0 THEN 1 ELSE 0 END +
    CASE WHEN atraso_mes_4 > 0 THEN 1 ELSE 0 END +
    CASE WHEN atraso_mes_5 > 0 THEN 1 ELSE 0 END +
    CASE WHEN atraso_mes_6 > 0 THEN 1 ELSE 0 END
  ) AS total_meses_atraso,

  GREATEST(
    atraso_mes_recente,
    atraso_mes_2,
    atraso_mes_3,
    atraso_mes_4,
    atraso_mes_5,
    atraso_mes_6
  ) AS atraso_maximo,

  CASE 
    WHEN atraso_mes_recente <= 0
     AND atraso_mes_2 <= 0
     AND atraso_mes_3 <= 0
     AND atraso_mes_4 <= 0
     AND atraso_mes_5 <= 0
     AND atraso_mes_6 <= 0
    THEN 1
    ELSE 0
  END AS cliente_pontual

FROM analise_cobranca.vw_credit_card_clean;

