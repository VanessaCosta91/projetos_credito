CREATE VIEW analise_cobranca.vw_credit_card_clean AS
SELECT 
  CAST(id AS INT64) AS id_cliente,
  limit_balance AS limite_credito,
  sex AS genero,
  education_level AS nivel_escolaridade,
  marital_status AS estado_civil,
  CAST(age AS INT64) AS idade,
  CAST(pay_0 AS INT64) AS atraso_mes_recente,
  CAST(pay_2 AS INT64) AS atraso_mes_2,
  CAST(pay_3 AS INT64) AS atraso_mes_3,
  CAST(pay_4 AS INT64) AS atraso_mes_4,
  CAST(pay_5 AS INT64) AS atraso_mes_5,
  CAST(pay_6 AS INT64) AS atraso_mes_6,
  bill_amt_1 AS valor_emitido_1,
  bill_amt_2 AS valor_emitido_2,
  bill_amt_3 AS valor_emitido_3,
  bill_amt_4 AS valor_emitido_4,
  bill_amt_5 AS valor_emitido_5,
  bill_amt_6 AS valor_emitido_6,
  pay_amt_1 AS valor_pago_1,
  pay_amt_2 AS valor_pago_2,
  pay_amt_3 AS valor_pago_3,
  pay_amt_4 AS valor_pago_4,
  pay_amt_5 AS valor_pago_5,
  pay_amt_6 AS valor_pago_6
FROM `bigquery-public-data.ml_datasets.credit_card_default`
WHERE 
  limit_balance IS NOT NULL
  AND limit_balance >= 0
  AND age >= 18
  AND CAST(sex AS INT64) IN (1,2)
  AND bill_amt_1 >= 0 AND bill_amt_2 >= 0 AND bill_amt_3 >= 0
  AND bill_amt_4 >= 0 AND bill_amt_5 >= 0 AND bill_amt_6 >= 0
  AND pay_amt_1 >= 0 AND pay_amt_2 >= 0 AND pay_amt_3 >= 0
  AND pay_amt_4 >= 0 AND pay_amt_5 >= 0 AND pay_amt_6 >= 0;

