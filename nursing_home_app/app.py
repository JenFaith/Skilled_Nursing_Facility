# IMPORT STATEMENTS
from flask import Flask, render_template, request, session
import pandas as pd
import numpy as np
import jinja2
import requests
import re
from .query import query_report
from .name_search import return_similar
import datetime
from datetime import date

# Instantiate Application
def create_app():
    """
    Function to deploy heroku application.
    Contains assorment of functions which control the inputs and outputs
    of interractive web application.
    """
    app = Flask(__name__)
    
    # Home Page
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/name_search', methods = ['GET', 'POST'])
    def name_search():
        return render_template('name_search.html')
    
    @app.route('/confirm', methods = ['GET', 'POST'])
    def recommendations():
        name=request.args.get('facility_name')
        num1, num2, num3, name1, name2, name3, ad1, ad2, ad3 = return_similar(name)
        return render_template('confirm.html', num1=num1, num2=num2, num3=num3, 
                               name1=name1, name2=name2, name3=name3, 
                               ad1=ad1, ad2=ad2, ad3=ad3)       
    

    
    @app.route('/location_search')
    def location_search():
        return render_template('index.html')
    
    @app.route('/report', methods = ['GET', 'POST'])
    def report():
        facility_name=request.args.get('facility_name')
        if request.method == "POST":
            name=request.args.get('facility_name')
        a = query_report(facility_name)
        number_of_expected_filings=a[0]
        sub = a[1]
        #plot_url=a[2]
        return render_template('report.html', 
                               facility_name = facility_name, 
                               number_of_expected_filings = number_of_expected_filings,
                               sub = sub)
    return app