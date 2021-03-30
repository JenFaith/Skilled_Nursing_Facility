import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

#TODO # Hide this my values later in .env file
database=os.getenv("database")
user=os.getenv("user")
password=os.getenv("password")
host=os.getenv("host")

conn = psycopg2.connect(
   database=database, user=user, password=password, host=host)

cursor = conn.cursor()

def create_user_table(conn = conn, cursor = cursor):
    """
    Created User Table in database
    """
    create_table ='''CREATE TABLE users(
        user_id SERIAL PRIMARY KEY,
        first_name VARCHAR(20) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
    )'''
    cursor.execute(create_table)
    cursor.close()
    conn.commit()

def save_user_session(conn = conn, cursor = cursor):
    """
    Created User Session Data Table in database
    """
    create_table ='''CREATE TABLE session_data(
        email VARCHAR(50) NOT NULL,
        facility VARCHAR(100) NOT NULL
    )'''
    cursor.execute(create_table)
    conn.commit()

def insert_user_data(name, email, password):
    """
    Inserts user's registration information into
    ElephantSQL database.
    """
    insert_command = ("INSERT INTO users(first_name, email, password)"
            "VALUES(%s, %s, %s)")
    data = (name, email, password)
    cursor.execute(insert_command, data)
    conn.commit()


def pull_user_data(email):
    """
    Returns user's registration information from elephantSQL Database
    if it exists.
    """
    query = "SELECT * FROM users WHERE email = '{}'".format(email)
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def login_process(email, password):
    """
    Returns user's registration information from elephantSQL Database
    if it exists.
    """
    query = "SELECT * FROM users WHERE email = '{}' and password = '{}'".format(email, password)
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def user_session_storage(email, facility_name):
    """
    Inserts user's session data into
    ElephantSQL database if it does not already exist.
    """
    # Check if session data has already been inserted
    # if it already exitst, it doesn't same data again to the database
    query = "SELECT * FROM session_data WHERE email = '{}' and facility = '{}'".format(email, facility_name)
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        pass
    else:
        insert_command = ("INSERT INTO session_data(email, facility)"
                "VALUES(%s, %s)")
        data = (email, facility_name)
        cursor.execute(insert_command, data)
        conn.commit()

