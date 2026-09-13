import logging
from datetime import datetime

# 1. Configure the log file location and formatting
logging.basicConfig(
    filename='/home/duckie-01/duck-coop-controller/log-file2.log',  # Path to your log file
    level=logging.INFO,                # Track INFO level messages and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 2. Write test messages to the log file
logging.info("The script started successfully.")
logging.warning("This is a warning message.")
logging.error("An error occurred.")
