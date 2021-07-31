import logging
logger = logging.getLogger(__name__)

def connection():
    logger.info("DB Connection")

if __name__ == '__main__':
    connection()
