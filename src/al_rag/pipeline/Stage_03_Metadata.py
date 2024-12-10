from src.al_rag.utils.common import log_and_handle_exceptions
from src.al_rag.components.metadata_generator import generate_metadata
from src.al_rag.config.configuration import load_config
import os

@log_and_handle_exceptions
def process_metadata():
    """
    Processes metadata using the input file specified in the config.
    """
    # Fetch CONFIG_PATH dynamically
    config_path = os.getenv("CONFIG_PATH")
    if not config_path:
        raise ValueError("CONFIG_PATH environment variable is not set")

    # Load configuration
    config = load_config(config_path)
    metadata_config = config.get('metadata', {})

    # Retrieve paths from the config
    input_file = metadata_config.get("input_file")
    metadata_folder = metadata_config.get("metadata_folder")
    tags = metadata_config.get("tags", [])

    # Call metadata generator with dynamic paths
    generate_metadata(file_path=input_file, metadata_folder=metadata_folder, tags=tags)
