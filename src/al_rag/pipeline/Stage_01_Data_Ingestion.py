from src.al_rag.components.DataIngestion import run_data_ingestion
from src.al_rag.constants import DEFAULT_CONFIG_FILE
from src.al_rag import logger

def execute_data_ingestion():
    """Execute the data ingestion pipeline."""
    try:
        logger.info("Starting the Data Ingestion Pipeline.")
        
        # Pass the configuration file path to the function
        run_data_ingestion(DEFAULT_CONFIG_FILE)
        
        logger.info("Data Ingestion Pipeline completed successfully.")
        
    except Exception as e:
        logger.error(f"Error in Data Ingestion Pipeline: {e}")