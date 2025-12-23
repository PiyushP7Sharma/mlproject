import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))

from ML_Project.logger import logging
from ML_Project.excceptions import CustomException

if __name__ == "__main__":
    logging.info("Execution started")

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
