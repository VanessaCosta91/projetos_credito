import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

# Função para validação e padronização os dados

def raw_para_staging(df: pd.DataFrame) -> pd.DataFrame:
    
    logger.info("Iniciando a transformação.")

    valida_dataframe(df)
    valida_schema(df)
    valida_regras(df)  
    
    df = padronizacao_tipos(df)
    df = adiciona_colunas(df)

    logger.info("Transformação concluída com sucesso.")

    return df

def valida_dataframe(df: pd.DataFrame) -> None:
        
        if df.empty:
            logger.error("DataFrame Vazio")
            raise ValueError("DataFrame Vazio")
        
        logger.info(f"DataFrame carregado com {len(df)} registros")
            
def valida_schema(df: pd.DataFrame) -> None:
    colunas_essenciais = {"Amount", "Class"}

    if not colunas_essenciais.issubset(df.columns):
        logger.error("Schema inválido: colunas essenciais ausentes")
        raise ValueError("Schema inválido")
    
    logger.info("Schema validado com sucesso")

def valida_regras(df: pd.DataFrame) -> None:
    
    if not df["Class"].isin([0,1]).all():
        logger.error("Valores encontrados na coluna Class são inválidos")
        raise ValueError("Valores inválidos em Class")
    
    if (df["Amount"] < 0).any():
        logger.error("Valores negativos")
        raise ValueError(("Amount não pode ser negativo"))
    
    logger.info("Validação de regras concluída com sucesso.")

def padronizacao_tipos(df: pd.DataFrame) -> pd.DataFrame:

    df["Amount"] = df["Amount"].astype(float)
    df["Class"] = df["Class"].astype(int)
    
    logger.info("Tipos de dados padronizados")
    return df

def adiciona_colunas(df: pd.DataFrame) ->pd.DataFrame:

    df["amount_log"] = np.log1p(df["Amount"])
    df["is_fraud"] = df["Class"] == 1

    logger.info("Colunas amount_log e is_fraud adicionadas")
    return df    