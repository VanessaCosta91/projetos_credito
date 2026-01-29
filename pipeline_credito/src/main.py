import logging
import pandas as pd
from extracao import extracao
from transformacao import bruto_para_preparacao
from analises import gerar_analise
from carga import carga_analises_sql

def configurar_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        filename="pipeline_credito/logs/pipeline.log",
        filemode="w"
    )

def carrega_dados_brutos(caminho_csv: str) -> pd.DataFrame:
    return pd.read_csv(caminho_csv)

def run_pipeline():

    logger = logging.getLogger(__name__)
    logger.info("Iniciando pipeline")

    dataset = "mlg-ulb/creditcardfraud"

    # Extração
    arquivos = extracao(dataset)
    logger.info(f"Arquivos disponíveis na pasta RAW: {arquivos}")

    caminho_csv = "pipeline_credito/data/raw/creditcard.csv"

    # Carrega dados de CSV em Dataframe
    df = carrega_dados_brutos(caminho_csv)
    logger.info("Dados brutos carregados em DataFrame")

    # Transformação
    df_transformado = bruto_para_preparacao(df)
    logger.info("Dados transformados")

    df_analises = gerar_analise(df_transformado)
    logger.info("Analises geradas.")

    carga_analises_sql(df_analises)
    logger.info("Dataframe carregado no banco de dados com sucesso")

if __name__ == "__main__":
    configurar_logging()
    run_pipeline()