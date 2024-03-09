import loggig
import os
from datetime import datetime

LOG_FILE=f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'
logs_path=os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.mkdir(logs_path, exit_ok=True)

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

loggig.basicConfig(
    filname=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)s %(levelname)s %(message)s',
    level=loggig.INFO
)