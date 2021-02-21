# Creating database instances

# Importing Data From CMS API

import numpy as np
import pandas as pd
import warnings
import requests
from bs4 import BeautifulSoup
import json
from sodapy import Socrata
import psycopg2

# TODO - Hide tokens
MyAppToken = '5YNrrmFobthjbfVSPQWEZWkkk'
username = 'jennifer.faith16@gmail.com'
password = 'Nashua1998!'

#Example authenticated client (needed for non-public datasets):
client = Socrata("data.cms.gov",
                 MyAppToken,
                 username,
                 password)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("s2uc-8wxp", limit = 1000000)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)

# Count data instances
df['submitted_data_counts'] = np.where(df['submitted_data']=='N', 0, 1)
df['passed_quality_counts'] = np.where(df['passed_quality_assurance']=="Y", 1, 0)

df = df.groupby(by = ['federal_provider_number', 'provider_name', 'provider_state', 'provider_city']).sum().reset_index()

df.to_csv('cms_data.csv')
