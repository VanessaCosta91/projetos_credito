-- Consolidar dados limpos + métricas financeiras + métricas comportamentais
CREATE OR REPLACE VIEW analise_cobranca.vw_dataset_final AS
SELECT
  c.*,
  p.valor_total_faturado,
  p.valor_total_pago,
  p.percentual_pago,
  p.saldo_liquido,
  p.nivel_eficiencia_pagamento,
  a.atraso_recente,
  a.total_meses_atraso,
  a.atraso_maximo,
  a.cliente_pontual
FROM analise_cobranca.vw_credit_card_clean c
LEFT JOIN analise_cobranca.vw_metricas_pagamento p
  ON c.id_cliente = p.id_cliente
LEFT JOIN analise_cobranca.vw_metricas_atraso a
  ON c.id_cliente = a.id_cliente;
