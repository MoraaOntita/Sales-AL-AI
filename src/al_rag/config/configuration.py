# loads the configuration values from config.yaml.

import yaml

def load_config(config_file):
    """Load configuration from a YAML file."""
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"The configuration file {config_file} was not found.")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML configuration file: {str(e)}")