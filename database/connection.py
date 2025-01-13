import os
import mysql.connector 
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

def getConnection():
    username = os.getenv('USERNAME')
    pw = os.getenv('PASSWORD')
    hostname = os.getenv('HOST')
    db = os.getenv('DATABASE')

    cnx = mysql.connector.connect(user = username, password = pw, host = hostname, database = db)

    cursor = cnx.cursor()
    logger.info(f'DB CONNECTION ESTABLISHED')
    return cnx, cursor