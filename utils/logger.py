import logging
import os
from datetime import datetime
from config.config import Config

class Logger:
    _loggers = {}
    
    @staticmethod
    def get_logger(name=__name__):
        if name in Logger._loggers:
            return Logger._loggers[name]
        
        # Create logs directory if it doesn't exist
        log_dir = os.path.dirname(Config.LOG_FILE)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, Config.LOG_LEVEL))
        logger.handlers.clear()
        
        # File handler with detailed format
        file_handler = logging.FileHandler(Config.LOG_FILE, mode='a')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        
        # Console handler
        if Config.CONSOLE_LOG:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(getattr(logging, Config.LOG_LEVEL))
            console_formatter = logging.Formatter(
                '%(asctime)s | %(levelname)-8s | %(message)s',
                datefmt='%H:%M:%S'
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)
        
        Logger._loggers[name] = logger
        return logger
    
    @staticmethod
    def log_test_start(test_name):
        logger = Logger.get_logger()
        logger.info("=" * 80)
        logger.info(f"TEST STARTED: {test_name}")
        logger.info("=" * 80)
    
    @staticmethod
    def log_test_end(test_name, status):
        logger = Logger.get_logger()
        logger.info("-" * 80)
        logger.info(f"TEST {status}: {test_name}")
        logger.info("-" * 80)
        logger.info("")