

import logging
import os
from datetime import datetime

# Step 1: File name create
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Logs folder ka path create karo
logs_path = os.path.join(os.getcwd(), "logs")

# Step 3: Agar folder exist nahi karta to bana do
os.makedirs(logs_path, exist_ok=True)

# Step 4: Complete log file path banao
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 5: Logging configuration set karo
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
