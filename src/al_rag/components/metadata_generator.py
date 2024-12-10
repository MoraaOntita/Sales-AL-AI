import os
import json
from datetime import datetime
from src.al_rag.utils.common import log_and_handle_exceptions
import logging
from src.al_rag.config.configuration import load_config

logger = logging.getLogger(__name__)

@log_and_handle_exceptions
def generate_metadata(file_path: str, metadata_folder: str, tags: list = None) -> dict:
    """
    Generates metadata for a text document and saves it as a JSON file.

    Args:
        file_path (str): Path to the text document (.txt).
        metadata_folder (str): Folder where metadata JSON will be saved.
        tags (list, optional): Custom tags related to the document.

    Returns:
        dict: The metadata dictionary.
    """
    try:
        # Load dynamic metadata configuration
        config_path = os.getenv("CONFIG_PATH")
        if not config_path:
            raise ValueError("CONFIG_PATH environment variable is not set")

        config = load_config(config_path)

        # Retrieve metadata parameters
        document_title = config['metadata'].get('document_title', "Untitled Document")
        author = config['metadata'].get('author', "Unknown")
        document_type = config['metadata'].get('document_type', "General")
        metadata_tags = tags or config['metadata'].get('tags', ["general"])

        # Ensure metadata directory exists
        os.makedirs(metadata_folder, exist_ok=True)

        # Read content from the .txt file
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found at: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            document_content = f.read()

        # Generate metadata
        metadata = {
            "document_id": os.path.basename(file_path),
            "document_title": document_title,
            "author": author,
            "document_type": document_type,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "word_count": len(document_content.split()),
            "document_preview": document_content[:500],
            "embedding_vector": None,  # Placeholder for embedding
            "tags": metadata_tags
        }

        # Save metadata to JSON
        metadata_file = os.path.join(metadata_folder, f"{metadata['document_id']}_metadata.json")
        with open(metadata_file, 'w', encoding='utf-8') as metadata_file_obj:
            json.dump(metadata, metadata_file_obj, indent=4)

        logger.info(f"Metadata saved successfully at {metadata_file}")
        return metadata

    except Exception as e:
        logger.error(f"Error generating metadata: {e}")
        raise
