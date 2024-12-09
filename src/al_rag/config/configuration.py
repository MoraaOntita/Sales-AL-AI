# loads the configuration values from config.yaml.

import yaml
from src.al_rag.custom_exceptions import ConfigurationError
from src.al_rag.utils.common import log_and_handle_exceptions
from typing import Dict

@log_and_handle_exceptions
def load_config(config_path: str) -> Dict:
    """Load a YAML configuration file.

    Args:
        config_path (str): Path to the YAML configuration.

    Returns:
        Dict: Configuration dictionary.

    Raises:
        ConfigurationError: If configuration loading fails.
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        if not config:
            raise ConfigurationError("Configuration file is empty.")
        return config
    except Exception as e:
        raise ConfigurationError(f"Failed to load configuration: {e}")