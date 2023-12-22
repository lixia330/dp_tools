import os
import sys
fwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(fwd,'libs'))

import time
import argparse
import libs.util
from pathlib import Path
from loguru import logger


if __name__ == '__main__': 
    # args handler
    parse = argparse.ArgumentParser(description="paramaters handler")
    parse.add_argument("--test", type=str, default="lixia")
    parse.add_argument("--test2", type=str, default="lixia2")
    args = parse.parse_args()


    # logger handler
    current_timestamp = time.strftime("%Y_%m_%d-%H_%M_%S")
    log_file = Path(f"./logs/{current_timestamp}.log")
    if not log_file.parent.exists():
        log_file.parent.mkdir(parents=True)
    logger.add(f"{log_file}", level="INFO", encoding="utf-8", enqueue=True)

    # 
    
    
    