from src.al_rag.entity.config_entity import DataIngestionConfig
from src.al_rag.config.configuration import load_config
from src.al_rag import logger
import gdown
import os

def run_data_ingestion(config_file):
    """Run the data ingestion process using values from the config file."""
    
    try:
        # Load the configuration from the YAML file
        config = load_config(config_file)
        data_config = config.get('data_ingestion', {})
        
        # If data_ingestion keys are missing, use defaults
        url = data_config.get('url', 'default_url')
        destination_folder = data_config.get('destination_folder', '/home/moraa-ontita/Documents/GenAI/Sales AI/artifacts/DataIngestion/')
        file_name = data_config.get('file_name', 'default_data_file.docx')
        
        # Create DataIngestionConfig instance
        data_ingestion_config = DataIngestionConfig(url, destination_folder, file_name)

        # Log the configuration being used
        logger.info(f"Starting data ingestion with config: {data_ingestion_config}")
        
        # Download the file
        download_file(data_ingestion_config)
        logger.info("Data ingestion completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred during data ingestion: {e}")

def download_file(config: DataIngestionConfig):
    """Download the file from the specified URL and save it to the destination folder."""
    try:
        file_id = config.url.split("/")[-2]
        download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
        
        # Ensure destination folder exists
        os.makedirs(config.destination_folder, exist_ok=True)
        
        file_path = os.path.join(config.destination_folder, config.file_name)
        
        # Download the file
        gdown.download(download_url, file_path, quiet=False)
        
        logger.info(f"File downloaded successfully: {file_path}")
    
    except Exception as e:
        logger.error(f"Error downloading file: {e}")