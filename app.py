import sys, os
sys.path.append(os.path.abspath("src"))
from ML_Project.components.data_ingestion import DataIngestion
from ML_Project.components.data_ingestion import DataIngestionConfig



from ML_Project.logger import logging
from ML_Project.exceptions import CustomException

if __name__ == "__main__":
    logging.info("Execution started")

    try:
       #data_ingestion = DataIngestion()
       data_ingestion = DataIngestion()
       data_ingestion.initiate_data_ingestion()
       

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
