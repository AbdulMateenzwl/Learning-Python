import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional
from datetime import datetime


class Config:
    """Application configuration class."""
    
    def __init__(self) -> None:
        """Initialize configuration by loading environment variables."""
        # Load environment variables from .env file
        load_dotenv()
        
        # API Configuration
        self.api_url: Optional[str] = os.getenv("API_URL")
        
        # Logging Configuration
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        
        # File paths
        self.output_dir: Path = Path("output")
        
    def setup_logging(self) -> None:
        """Configure application logging with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f'app_{timestamp}.log'
        
        logging.basicConfig(
            level=getattr(logging, self.log_level.upper()),
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(log_filename)
            ]
        )
        
    def validate_config(self) -> bool:
        """Validate required configuration values."""
        if not self.api_url:
            logging.error("API_URL environment variable is not set.")
            return False
        return True


# Global configuration instance
config = Config()

if not config.validate_config():
    raise ValueError("Invalid configuration")
