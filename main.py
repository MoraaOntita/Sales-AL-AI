from src.al_rag.pipeline.Stage_01_Data_Ingestion import execute_data_ingestion
from src.al_rag.pipeline.Stage_02_Data_Loader import load_data
from src.al_rag import logger

def run_stage(stage_name: str, stage_function: callable):
    """
    Runs a specific pipeline stage with logging and exception handling.

    Args:
        stage_name (str): Name of the pipeline stage.
        stage_function (callable): Function to execute for the stage.
    """
    try:
        logger.info(f">>>>>> Stage {stage_name} started <<<<<<")
        
        # Execute the stage function
        stage_function()
        
        logger.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"Error in the {stage_name}: {e}")
        logger.exception(e)  # Log the full traceback for debugging

if __name__ == "__main__":
    logger.info("Pipeline Execution Started.")
    
    # Define pipeline stages
    stages = [
        {"name": "Data Ingestion Stage", "function": execute_data_ingestion},
        {"name": "Data Loader Stage", "function": load_data},
    ]
    
    # Execute all pipeline stages sequentially
    for stage in stages:
        run_stage(stage["name"], stage["function"])
    
    logger.info("Pipeline Execution Completed Successfully.")