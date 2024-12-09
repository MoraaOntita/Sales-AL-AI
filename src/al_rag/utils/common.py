from functools import wraps
from src.al_rag import logger

def log_and_handle_exceptions(func):
    """Decorator to log and handle exceptions in any function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"Executing: {func.__name__}")
            result = func(*args, **kwargs)
            logger.info(f"Execution successful: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise e
    return wrapper