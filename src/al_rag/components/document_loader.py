import os
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from src.al_rag.custom_exceptions import DocumentLoadingError
from src.al_rag.utils.common import log_and_handle_exceptions
from functools import lru_cache
from typing import List
from langchain.docstore.document import Document
import logging

# Set up logging (if you haven't already configured it globally)
logger = logging.getLogger(__name__)

@log_and_handle_exceptions
@lru_cache(maxsize=10)  # Caching loaded documents for reuse
def load_document(file_path: str, save_to: str = None) -> List[Document]:
    """Loads a .docx document, caches it, and optionally saves it to a specified location.

    Args:
        file_path (str): Path to the .docx file.
        save_to (str): Path to save the loaded document.

    Returns:
        List[Document]: List of LangChain documents.

    Raises:
        DocumentLoadingError: If the document fails to load.
    """
    try:
        # Load the document using UnstructuredWordDocumentLoader
        loader = UnstructuredWordDocumentLoader(file_path)
        documents = loader.load()

        if not documents:
            raise DocumentLoadingError("No content found in the document.")
        
        # If save_to is provided, save the document content as text
        if save_to:
            # Ensure the directory exists before attempting to save
            save_dir = os.path.dirname(save_to)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir, exist_ok=True)
            
            # Save the content of the document to a file
            try:
                with open(save_to, 'w') as file:
                    for doc in documents:
                        file.write(doc.page_content + "\n\n")  # Save each document's content
                logger.info(f"Document content saved to: {save_to}")
            except Exception as e:
                logger.error(f"Failed to save document to {save_to}: {e}")
                raise DocumentLoadingError(f"Failed to save document: {e}")

        return documents
    except Exception as e:
        logger.error(f"Failed to load document from {file_path}: {e}")
        raise DocumentLoadingError(f"Failed to load document: {e}")
