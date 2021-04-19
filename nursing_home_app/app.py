# IMPORT STATEMENTS
from flask import Flask, render_template, request, session
from flask_session import Session
# TODO # from flask_mail import Mail, Message
from os import getenv
import pandas as pd
import numpy as np
import jinja2
import requests
import re
from .query import facility_number, Report
from .name_search import return_similar
from .user_database import insert_user_data, pull_user_data, login_process, user_session_storage, pull_user_facils
import datetime
from datetime import date


def create_app():
    """
    Function to deploy heroku application.
    Contains assorment of functions which control the inputs and outputs
    of interractive web application.
    """
    app = Flask(__name__)
    app.config["SESSION_PERMANENT"]=False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    
    # Home Page
    @app.route('/')
    def home():
        """
        Basic homepage for application.
        Allows users to login/register and chose whether to search for facilities
        by name or by location.
        """
        return render_template('home.html')
    
    @app.route('/register', methods = ['GET', 'POST'])
    def register():
        """
        Route to register new user.
        This page will continue to rerender the register.html until the inputs are as expected
        OR until the user goes to the login page instead.
        1) Checks that form has been fully filled out
        2) Checks if there is an existing accout
        3) If there is an existing account, users are encouraged to login instead.
        4) Else, new account is created
        5) Initializes session
        """
        # Start by having no special message on register page
        message = ' '
        # Return customized message if one piece of the form is missing
        if request.method == "POST":
            name = request.form.get('name')
            if not name:
                return render_template("register.html", message = 'You\'re missing a name!')
            email = request.form.get('email')   
            if not email:
                return render_template("register.html", message = 'You\'re missing an email!')
            password = request.form.get('password')
            if not password:
                return render_template("register.html", message = 'You\'re missing a password!')
            # Check if account already exists
            if 'name' in request.form and 'email' in request.form and 'password' in request.form:
                user_info = pull_user_data(email)
            if user_info:
                return render_template("register.html", message = 'This account already exists.')
            else:
                # Store values in a consistent way
                insert_user_data(name.title(), email.lower(), password)
                session['name'] = name.title()
                session['email'] = email.lower()
                message = "Thanks for registering, " + name + '!'
        return render_template('register.html', message = message)
    
    @app.route('/login', methods = ['GET','POST'])
    def login():
        """
        Route to login user with an existing account.
        1) Checks that form has been filled out
        2) Checks if there is an existing accout
        3) Initializes session
        """
        #Message is empty when user firsts gets to page
        message = ''
        # Take user inputs
        if request.method == 'POST':
            email = request.form.get('email')   
            if not email:
                return render_template("login.html", message = 'You\'re missing an email!')
            password = request.form.get('password')
            if not password:
                return render_template("login.html", message = 'You\'re missing a password!')
            # Check if account already exists
            if 'email' in request.form and 'password' in request.form:
                user_info = login_process(email, password)
                if user_info:
                    session['name'] = user_info[0][1]
                    return render_template("login.html", message = 'Welcome back, ' + session['name'] + '!')
                else:
                    return render_template("login.html", message = 'Oops! Something is not quite right.')
                # TODO allowe users to reset password
        return render_template("login.html", message = message)
   
    
    @app.route('/name_search', methods = ['GET', 'POST'])
    def name_search():
        """
        Form to pull name of facility.
        Pull top 3 similar facility names and let user choose the one they meant or retype name.
        """
        # No message at first
        message = ''
        name_1=''
        name_2= ''
        name_3= ''
        ad_1= ''
        ad_2= ''
        ad_3= ''
        htmlvar_1 = ''
        htmlvar_2 = ''
        htmlvar_3 = ''
        if request.method == 'POST':
            facil_name=request.form.get('facility_name')
            num1, num2, num3, name1, name2, name3, ad1, ad2, ad3 = return_similar(facil_name)
            # return suggested names with addresses 
            # plus, make them slightly less obnoxious to read
            return render_template('name_search.html', message = "Did you mean:",
                                   name1=name1.title(), name2=name2.title(), name3=name3.title(),
                                   ad1=' at ' + ad1.title(), ad2=' at ' + ad2.title(), ad3=' at ' + ad3.title(), 
                                   # Returns variable href tag to allow user to click on facility name
                                   # And be moved to a report on that facility.
                                   # Doing it this way also allows the application to capture the users selection
                                   # See name_search.html to see how this variable was used
                                   htmlvar1 = '/report?facility_name='+name1.replace(' ', '+'), 
                                   htmlvar2 = '/report?facility_name='+name2.replace(' ', '+'), 
                                   htmlvar3 = '/report?facility_name='+name3.replace(' ', '+'))
        # TODO # In final stages, make these buttons instead of hyperlinking text!
        return render_template('name_search.html', message = message,
                               name1=name_1, name2=name_2, name3=name_3, 
                               ad1=ad_1, ad2=ad_2, ad3=ad_3, 
                               htmlvar1=htmlvar_1, htmlvar2=htmlvar_2, htmlvar3=htmlvar_3)
    
    
    @app.route('/location_search')
    def location_search():
        """
        Allows user to search by map for a facility. 
        """
        return render_template('location_search.html')
    
    @app.route('/state')
    def state():
        state=request.args.get('State')
        return render_template('states/' + state + '.html')
    
    @app.route('/report', methods = ['GET', 'POST'])
    def report():
        """ 
        Returns report on facility.
        """
        facility_name=request.args.get('facility_name')
        session['save']=facility_name
        
        # Return provider number for facility name
        prov_num = facility_number(facility_name)
        # Generate report
        facility_rep = Report(prov_num)
        # Return covid report
        covid_rep = facility_rep.covid_report()
        # a = query_report(facility_name)
        # number_of_expected_filings=a[0]
        # sub = a[1]
        return render_template('report.html', 
                               facility_name = facility_name,
                               covid_report = covid_rep)
                            #    number_of_expected_filings = number_of_expected_filings,
                            #    sub = sub)
    
    @app.route('/myfacilities', methods = ['GET', 'POST'])
    def user_page():
        facility_name = session['save']
        email = session['email']
        user_session_storage(email, facility_name)
        user_data = pull_user_facils(email)
        return render_template('user_page.html', user_data = user_data)
    
    return app