import os
from src.al_rag.config.configuration import load_config

# Dynamically determine the base directory of the project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

# Correct path to the configuration file
DEFAULT_CONFIG_FILE = os.path.join(BASE_DIR, "config", "config.yaml")

# Load global configurations
global_config = load_config(DEFAULT_CONFIG_FILE)
CONFIG_PATH = global_config.get("global", {}).get("config_path", DEFAULT_CONFIG_FILE)

# Set CONFIG_PATH environment variable dynamically
os.environ["CONFIG_PATH"] = CONFIG_PATH
