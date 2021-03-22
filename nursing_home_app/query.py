import pandas as pd
import numpy as np
import requests
import re
import sqlite3
import datetime
from datetime import date
#import StringIO
import base64

def query_report(facility_name):
    # ACCESS PROV NUM FROM DATABASE
    con = sqlite3.connect('nhs_descriptions.sqlite3')
    cur = con.cursor()
    item = (facility_name,)
    cur.execute('SELECT  federal_provider_number FROM Data WHERE provider_name = ?', item)
    numbers = cur.fetchone()
    number = numbers[0]
    get = 'https://data.cms.gov/resource/s2uc-8wxp.json?federal_provider_number={facility}'.format(facility = number)
    response = requests.get(get)
    dictionary = response.json()
    df = pd.DataFrame(dictionary)
    # Calculate the number of expected filings
    number_of_expected_filings = int(abs(datetime.date(2020, 5, 24)-date.today()).days/7)
    # Report number of actual filings
    sub = df['submitted_data'].value_counts().sort_values(axis='index')[0]
    
    # Visualize Resident Covid-19 Cases
    #img = StringIO.StringIO()
    # plt.plot(df['residents_weekly_covid_19'], color='red', marker='o')
    # plt.title('Reported Resident Covid-19 Cases Per Week', fontsize=14)
    # plt.xlabel('Week', fontsize=14)
    # plt.ylabel('Cases', fontsize=14)
    # plt.savefig(img, format='png')
    # plt.close()
    # img.seek(0)
    # plot_url = base64.b64encode(img.getvalue())
    return [number_of_expected_filings, sub]


#Running Tests
a = query_report('AHC LEWIS COUNTY')
number_of_expected_filings=a[0]
sub = a[1]
print(number_of_expected_filings)
print(sub)