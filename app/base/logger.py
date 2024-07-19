import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name, log_file, max_bytes=2048000, backup_count=5, level=logging.INFO):
    """Function to set up a logger with a rotating file handler."""
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    
    handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    # Add StreamHandler to also output logs to console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    return logger

# Create and configure the logger for the application
def create_logger(log_dir="logs", log_filename="app.log", max_bytes=2048000, backup_count=5, level=logging.INFO):
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_filename)
    logger = setup_logger('app_logger', log_path, max_bytes, backup_count, level)
    return logger

logger = None  # Global logger variable

def initialize_logger():
    global logger
    if logger is None:
        logger = create_logger()
    return logger

# Initialize the logger when this module is imported
initialize_logger()