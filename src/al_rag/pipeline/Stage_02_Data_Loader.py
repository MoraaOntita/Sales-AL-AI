from src.al_rag.components.document_loader import load_document
from src.al_rag.config.configuration import load_config
from src.al_rag.utils.common import log_and_handle_exceptions
from src.al_rag import logger
from src.al_rag.constants import CONFIG_PATH

@log_and_handle_exceptions
def load_data():
    """Pipeline to load document data."""
    # Load configuration dynamically
    config = load_config(CONFIG_PATH)
    document_path = config.get('document_loader', {}).get('file_path')
    save_path = config.get('document_loader', {}).get('save_path')

    if not document_path:
        logger.error("Document path not found in configuration.")
        return
    
    if not save_path:
        logger.error("Save path not found in configuration.")
        return

    # Load and save the document
    documents = load_document(document_path, save_to=save_path)

    logger.info(f"Document loaded and saved to: {save_path}")
    logger.info(f"Document loaded with {len(documents)} page(s).")
    logger.info(f"Content Preview: {documents[0].page_content[:100]}")
