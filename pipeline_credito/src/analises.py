import logging
import pandas as pd

logger = logging.getLogger(__name__)

def gerar_analise (df: pd.DataFrame) -> pd.DataFrame:
    df["faixa_valor"] = pd.qcut(df["Amount"],  q=5, labels=["muito_baio", "baixo", "medio", "alto", "muito_alto"])

    logger.info("Criando DataFrame agregado")
    df_analises = (df.groupby("faixa_valor").agg(
                qtde_transacoes=("Amount", "count"),
                valor_total_transacoes=("Amount", "sum"),
                total_fraudes=("is_fraud", "sum"),
                percentual_fraude=("is_fraud", "mean")
                
    ))
    logger.info("Novo Dataframe criado com sucesso")

    return df_analises


