from db_setup import create_logs_db
from system_info import run_system_logging
from sql_logger import logger

def run_pipeline():
    create_logs_db()
    logger.info("Starting system info collection...")
    run_system_logging()
    logger.info("System info collection complete.")

if __name__ == "__main__":
    run_pipeline()
