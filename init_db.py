import os
import json
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Default values for if the
# code in the `try` block does not run.
conn = None 
cur = None 
try:
        conn = psycopg2.connect(
        host="localhost",
        database="prime_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
	port=5432)

        
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS belyi")
        
        create_script = ''' CREATE TABLE IF NOT EXISTS belyi (
                                label varchar(100),
                                index int NOT NULL,
                                critical_points varchar(32672),
                                status char(30),
                                group_name varchar(30)) '''
        cur.execute(create_script)

        file = open('/home/tesfa/prime/belyi_data.json', "r")

        file_str_form = file.read()

        list_of_dict = list(eval(file_str_form))

        columns = list_of_dict[0].keys()
        query = "INSERT INTO belyi ({}) VALUES %s".format(','.join(columns))

        for dictionary in list_of_dict:
                if "critical_points" not in dictionary.keys():
                        dictionary["critical_points"] = "NULL"
                for value in dictionary.values():
                        if len(value) >= 1000:
                                print(len(value))

        # convert list_of_dict's values to sequence of sequences
        values = [[value for value in dictionary.values()] for dictionary in list_of_dict]
        print(len(values), "values")
        print(len(columns), "keys")
        execute_values(cur, query, values)
        
        # We need to commit, or save, our transactions with the database
        conn.commit()
except Exception as error:
        print(error)
finally: 
        # Whether there is an exception, `finally`
        # blocks execute regardless.
        # Whenever we open a connection or cursor, we must close 
        # them once done.
        if cur is not None:
                # This means that the cursor was opened
                cur.close()
        if conn is not None:
                # This means that the connection was opened
                conn.close()

        
