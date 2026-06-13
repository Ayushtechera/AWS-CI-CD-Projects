import logging 
import os 
from datetime import datetime 


''' 
Program Start
      ↓
Current Time se
LOG_FILE banao
      ↓
create log folder path 
      ↓
create log folder 
      ↓
create LOG_FILE_PATH
      ↓
logging.basicConfig()
(Logging configure)
      ↓
logging.info(...)
      ↓
save Message in log file 
'''


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logs_path = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(logs_path,exist_ok=True)  

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)
print(LOG_FILE_PATH)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

