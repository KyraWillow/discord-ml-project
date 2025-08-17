# Import required libraries.
import yaml
import joblib
import pandas as pd

from datetime import datetime

CONFIG_DIR = "../config/config.yaml"


# Function to load configuration file.
def load_config(config_dir: str = CONFIG_DIR) -> dict:
    """
    Load the configuration file.
    
    Parameters:
    ----------
    config_dir : str
        The configuration file location.
        
    Returns:
    -------
    config : dict
        The loaded configuration file.
    """
    # Try to load the yaml file.
    try:
        with open(config_dir, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError as err:
        raise RuntimeError("Configuration file not found in the path.")
    
    # Return the loaded config file.
    return config


# Function to serialize data.
def pickle_dump(data: pd.DataFrame, path: str):
    """
    Serialize data into pickle file.
    
    Parameters:
    ----------
    data : pd.DataFrame
        The loaded data.
        
    path : str
        The destination path.
        
    Returns:
    -------
    None
    """
    # Serialize the data into the path.
    joblib.dump(data, path)
    print("Data serialized.")
    

# Function to deserialize data.
def pickle_load(file_path: str):
    """
    Deserialize pickle file into Python object.
    
    Parameters:
    ----------
    file_path : str
        The path to pickle file.
        
    Returns:
    -------
    Any Python object.
    """
    return joblib.load(file_path)


config = load_config()
PRINT_DEBUG = config["print_debug"]


# Function for logging related.
def time_stamp():
    """Return the current date and time."""
    return datetime.now()

def print_debug(message):
    """Check whether user wants to use print or not."""
    if PRINT_DEBUG:
        print(time_stamp(), message)
    