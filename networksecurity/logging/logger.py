import logging
import os
from datetime import datetime

LOG_FIle = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs",LOG_FIle)
os.makedirs(log_path,exist_ok=True)

LOG_FIle_Path = os.path.join(log_path,LOG_FIle)

logging.basicConfig(level=logging.INFO,filename=LOG_FIle_Path,format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")