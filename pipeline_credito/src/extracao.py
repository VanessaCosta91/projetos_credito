from kaggle.api.kaggle_api_extended import KaggleApi
import os
import logging

logger = logging.getLogger(__name__)

def extracao (dataset) -> list:

    try:    
        logger.info(f'Iniciando o downlowd do dataset do Kaggle')
        
        # Autenticação
        api = KaggleApi()
        api.authenticate()
        logger.info(f'Autenticação realizada com sucesso.')

        # Caminho pasta que armazena dados brutos
        caminho = "data/raw"
        os.makedirs(caminho, exist_ok=True)

        # Fazer Dowlond dataset
        api.dataset_download_files(
            dataset,
            path=caminho,
            unzip=True
        )
        
        arquivos = os.listdir(caminho)
        logger.info(f'Extração concluída. Arquivos: {arquivos}')

        return arquivos
       
    except Exception as e:
        logger.exception('Erro durante extração dos dados.')
        raise
    
