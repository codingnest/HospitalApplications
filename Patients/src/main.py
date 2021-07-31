#import Patients.src.backend.db_connection
#import Patients.src.backend.db_connection as m
#from Patients.src.backend import db_connection
from Patients.src.backend.db_connection import connection
from Patients.src.frontend.template import frontend_template
from Patients.src.controller.middleware import mvc_middleware
#from Patients.src.backend.db_connection import *
import numpy, pytest_bdd
import logging, argparse

from logging.handlers import TimedRotatingFileHandler


if __name__ == '__main__':
    #Patients.src.backend.db_connection.connection()
    #m.connection()
    #db_connection.connection()

    #Argparse configuration
    parser = argparse.ArgumentParser()

    requiredNamed = parser.add_argument_group("Required named argument")
    requiredNamed.add_argument('-e','--email_id', dest= 'email_id',
                               help="please enter the email address",
                               required=True, nargs='+')
    args = parser.parse_args()
    email_address = args.email_id

    #logging Configuration
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(lineno)d %(message)s', datefmt='%Y-%m-%d--%H:%M:%S')
    fileHandler = logging.FileHandler(filename=r'C:\Users\admin\PycharmProjects\Hospitalapplications\Patients\log\app.log')
    fileHandler.setFormatter(formatter)

    #logname = r'C:\Users\admin\PycharmProjects\Hospitalapplications\Patients\log\app.log'
    #handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
    #handler.suffix = "%Y%m%d"
    #logger.addHandler(handler)
    logger.setLevel(level=logging.DEBUG)
    logger.addHandler(fileHandler)

    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.CRITICAL)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)

    logger.debug("Starting...")
    logger.debug("Call to connection method...")
    connection()
    frontend_template()
    mvc_middleware()

    logger.info("Email address - {}".format(email_address))

    #logger.critical("General Error")