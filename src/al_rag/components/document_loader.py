from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from src.al_rag.custom_exceptions import DocumentLoadingError
from src.al_rag.utils.common import log_and_handle_exceptions
from functools import lru_cache
from typing import List
from langchain.docstore.document import Document

@log_and_handle_exceptions
@lru_cache(maxsize=10)  # Caching loaded documents for reuse
def load_document(file_path: str) -> List[Document]:
    """Loads a .docx document and caches it.

    Args:
        file_path (str): Path to the .docx file.

    Returns:
        List[Document]: List of LangChain documents.

    Raises:
        DocumentLoadingError: If the document fails to load.
    """
    try:
        loader = UnstructuredWordDocumentLoader(file_path)
        documents = loader.load()
        if not documents:
            raise DocumentLoadingError("No content found in the document.")
        return documents
    except Exception as e:
        raise DocumentLoadingError(f"Failed to load document: {e}")