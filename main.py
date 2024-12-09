from src.al_rag.pipeline.Stage_01_Data_Ingestion import execute_data_ingestion
from src.al_rag import logger

if __name__ == "__main__":
    STAGE_NAME = "Data Ingestion Stage"
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        
        # Run the entire data ingestion pipeline
        execute_data_ingestion()

        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.error(f"Error in the {STAGE_NAME}: {e}")
        logger.exception(e)  # Log the full traceback of the error