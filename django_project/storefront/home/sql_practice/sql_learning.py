import os
from pickle import TRUE
import mysql.connector
from mysql.connector import Error
import pandas as pd
import logging
from datetime import datetime

# --------------------LOGGER SETUP--------------------

CURR_DATETIME = datetime.now().strftime(f"%d_%m_%Y_%H_%M_%S")
os.makedirs(r"sql_practice/logs", exist_ok=True)
os.chdir(r"sql_practice/logs")
FILENAME_LOG = f"log_{CURR_DATETIME}.log"
FORMAT = "\x1b[31;20m" + "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
F_FORMAT = logging.Formatter("[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s")
fh = logging.FileHandler(FILENAME_LOG, mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(F_FORMAT)
logger = logging.getLogger()
logger.addHandler(fh)
# ----------------- LOGGER SETUP DONE-----------------
class SQLExecution:


    def connect_with_server(self, hostname, username, password, db_name = None):
        conn = None
        try:
            conn = mysql.connector.connect(host = hostname, user = username, passwd = password, database = db_name)
            logger.info(f"Connection established successfully.")
        except Error as e:
            logger.info(f"{e}")
            raise e
        return conn

    def create_database(self, conn, query):
        cur = conn.cursor()
        try:
            cur.execute(query)
            logger.info(f"Database created successfully.")
        except Error as e:
            logger.info(f"{e}")
            raise e
        
    def execute_query(self, conn, query):
        cur = conn.cursor()
        try:
            cur.execute(query)
            conn.commit()
            # conn.close()
            logger.info(f"Query executed successfully.")
            return True, "Query executed successfully."
        except Error as e:
            logger.info(f"{e}")
            return False, e.__str__()
            # raise e

    def read_query(self, conn, query):
        cur = conn.cursor()
        result = None
        try:
            cur.execute(query)
            result = cur.fetchall()
            logger.info(f"Fetch Successful.")
            return result
        except Error as e:
            logger.info(f"{e}")
            raise e

    
if __name__ == "__main__":
    # query = """SELECT * FROM `mytable`;"""
    query = """
            CREATE TABLE user_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            pwds VARCHAR(40) NOT NULL);
            """
    sql_obj = SQLExecution()
    conn = sql_obj.connect_with_server("localhost", "root", "0599", "mydb")

    result, msg = sql_obj.execute_query(conn, query)
    print(msg)
    # res_db = []
    # for res in result:
    #     res = list(res)
    #     res_db.append(res)

    # columns = ["pk_column", "field1", "Unnamed 0", "business_code", "cust_number", "name_customer", "clear_date", "business_year", "doc_id",
    #         "posting_date", "document_create_date", "document_create_date1", "due_in_date", "invoice_currency", "document_type", "posting_id",
    #         "area_business", "total_open_amount", "baseline_create_date", "cust_payment_terms", "invoice_id", "isOpen", "delay", "predicted_payment_date",
    #         "aging_bucket"]
    # df = pd.DataFrame(res_db, columns=columns)
    # logger.info(f"{df.head()}")




