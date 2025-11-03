import logging
import os
from datetime import datetime


LOGS_DIR= "logs"
## Creates the log directory in case it doesnt exists, avoids trowing an exception if it already exists
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR,f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
  filename=LOG_FILE,  # Determines where the messages will be written
  format='%(asctime)s - %(levelname)s - %(message)s', ## Determines the format of the messages
  level=logging.INFO ### In case we want to logg INFO --- CRITICAL, WARNING, ERROR, DEBUG out of the logs in this case

)

## Basic types of loggings
### INFO, WARNING, ERROR
### time - INFO - message <-----example structure

def get_logger(name):
  logger= logging.getLogger(name)
  logger.setLevel(logging.INFO)
  return logger