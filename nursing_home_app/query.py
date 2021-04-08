import pandas as pd
import numpy as np
import requests
import re
import sqlite3
import datetime
from datetime import date
#import StringIO
import base64

def facility_number(fac_name):
    """
    Find provider number from facility name
    """
    con = sqlite3.connect('nhs_descriptions.sqlite3')
    cur = con.cursor()
    item = (fac_name,)
    cur.execute('SELECT federal_provider_number FROM Data WHERE provider_name = ?', item)
    numbers = cur.fetchone()
    fac_num = numbers[0]
    return fac_num



class Report:
    """
    Defines report for each facility.
    """
    # initialize sturcture
    def __init__(self, fac_num):
        self.fac_num = fac_num
        
    def covid_report(self):
        """
        Report based on covid data
        """
        # Grab data from csm api and transform it into easy to work with data structure
        get = 'https://data.cms.gov/resource/s2uc-8wxp.json?federal_provider_number={facility}'.format(facility = self.fac_num)
        response = requests.get(get)
        dictionary = response.json()
        df = pd.DataFrame(dictionary)
        
        # GENERATE REPORT DATA
        number_of_expected_filings = int(abs(datetime.date(2020, 5, 24)-date.today()).days/7)-1
        submitted = df['submitted_data'].value_counts().sort_values(axis='index')[0]
        mean_num_residents = int(df['total_number_of_occupied'].astype(int).mean().round())
        total_covid_cases_confirmed = df['residents_weekly_confirmed'].astype(int).sum()
        percent_of_residents_with_covid = ((total_covid_cases_confirmed/mean_num_residents)*100).round(2)
        total_covid_deaths_confirmed = df['residents_weekly_covid_19'].astype(int).sum()
        percent_of_residents_covid_deaths = ((total_covid_deaths_confirmed/mean_num_residents)*100).round(2)
        nursing_shortage = sum(df['shortage_of_nursing_staff']=='Y')
        clinical_staff_shortage = sum(df['shortage_of_clinical_staff']=='Y')
        aid_shortage = sum(df['shortage_of_aides']=='Y')
        total_occupied_beds = int(df['total_number_of_occupied'][df['week_ending']==df['week_ending'].max()].values[0])
        
        # Return report in dictionary so it's easy to use/access later
        return {"number_of_expected_filings" : number_of_expected_filings,
                "submitted" :submitted,
                "mean_num_residents" :mean_num_residents,
                "total_covid_cases_confirmed" :total_covid_cases_confirmed,
                "percent_of_residents_with_covid" :percent_of_residents_with_covid,
                'percent_of_residents_covid_deaths' : percent_of_residents_covid_deaths,
                'nursing_shortage' : nursing_shortage,
                'clinical_staff_shortage' : clinical_staff_shortage,
                'aid_shortage' : aid_shortage,
                'total_occupied_beds' : total_occupied_beds}
    
    # TODO # How would I get these to automatically find the newest api connection in the furture?
    def health_vilations_report(self):
        """
        Report on Health Violations
        """
        pass
     
    def ownership_report(self):
        """
        Report on Ownership Data
        """
        pass
    
    def staffing_report(self):
        """
        Report on Staffing Data
        """
        pass
    
## DELETE OUT LATER
def query_report(facility_name):
    # ACCESS PROV NUM FROM DATABASE
    con = sqlite3.connect('nhs_descriptions.sqlite3')
    cur = con.cursor()
    item = (facility_name,)
    cur.execute('SELECT federal_provider_number FROM Data WHERE provider_name = ?', item)
    numbers = cur.fetchone()
    number = numbers[0]
    get = 'https://data.cms.gov/resource/s2uc-8wxp.json?federal_provider_number={facility}'.format(facility = number)
    response = requests.get(get)
    dictionary = response.json()
    df = pd.DataFrame(dictionary)
    # Calculate the number of expected filings
    number_of_expected_filings = int(abs(datetime.date(2020, 5, 24)-date.today()).days/7)-1
    # Report number of actual filings
    sub = df['submitted_data'].value_counts().sort_values(axis='index')[0]
    return [number_of_expected_filings, sub]


# TESTING REPORTS
# item = facility_number('EGRET COVE CENTER')
# facility = Report(item)
# covid = facility.covid_report()