import logging

# Set basic config
logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message")      # Will not show (level is INFO)
logging.info("This is an info message")       # Will show
logging.warning("This is a warning")          # Will show
logging.error("This is an error")             # Will show
logging.critical("Critical failure!")         # Will show
