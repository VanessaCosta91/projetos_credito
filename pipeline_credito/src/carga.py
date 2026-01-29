import pandas as pd
import logging
from pathlib import Path
import sqlite3

logger = logging.getLogger(__name__)

# Função para salvar dados tratados em banco de dados SQL
def carga_analises_sql(
    df: pd.DataFrame,       
    caminho_db: str = "pipeline_credito/data/database/pipeline_credito.db",
    nome_tabela: str = "analise_fraude"
) -> None:
    
    logger.info("Iniciando carga do Dataframe no banco de dados SQL.")

    if df.empty:
        logger.error("Dataframe Vazio.")
        raise ValueError("Não é possível carregar dados vazios")
    
    # Garantte de existência do pasta
    Path(caminho_db).parent.mkdir(parents=True, exist_ok=True)

    # Conexão com sqlite
    conn = sqlite3.connect(caminho_db)

    try:
        df.to_sql(name=nome_tabela, con=conn, if_exists="replace", index=False)

        logger.info("Dados carregados com sucesso.")

    finally:
        conn.close
        logger.info("Conexão com banco de dados encerrada.")