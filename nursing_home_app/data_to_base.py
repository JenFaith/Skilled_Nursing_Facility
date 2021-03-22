import sqlite3
import psycopg2
import pandas as pd

#Creating sqlite3 database of names/addresses
df = pd.read_csv('nhs_descriptor.csv')
conn = sqlite3.connect('nhs_descriptions.sqlite3')
df.to_sql('Data', con=conn, if_exists='replace', index=True)
# t_curs = conn.cursor()