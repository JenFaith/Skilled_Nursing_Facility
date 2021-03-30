# IMPORT STATEMENTS
from flask import Flask, render_template, request, session
from flask_session import Session
# TODO # from flask_mail import Mail, Message
# Email reports to users??? ^^^
from os import getenv
import pandas as pd
import numpy as np
import jinja2
import requests
import re
from .query import query_report
from .name_search import return_similar
from .user_database import insert_user_data, pull_user_data, login_process
import datetime
from datetime import date

# Instantiate Application
# All routes the application follows
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
        if request.method == 'POST':
            facil_name=request.form.get('facility_name')
            num1, num2, num3, name1, name2, name3, ad1, ad2, ad3 = return_similar(facil_name)
            # return suggested names with addresses 
            # plus, make them slightly less obnoxious to read
            return render_template('name_search.html', message = "Did you mean:",
                                   name1=name1.title() + 'at', name2=name2.title() + 'at', name3=name3.title() + 'at',
                                   ad1=ad1.title(), ad2=ad2.title(), ad3=ad3.title())    
        return render_template('name_search.html', message = message,
                               name1=name_1, name2=name_2, name3=name_3, 
                               ad1=ad_1, ad2=ad_2, ad3=ad_3)    
    
    # @app.route('/confirm', methods = ['GET', 'POST'])
    # def recommendations():
    #     """
    #     Confirms application has found correct facility name.
    #     """
    #     facil_name=request.args.get('facility_name')
    #     num1, num2, num3, name1, name2, name3, ad1, ad2, ad3 = return_similar(facil_name)
        
    #     return render_template('confirm.html', 
    #                            name1=name1, name2=name2, name3=name3, 
    #                            ad1=ad1, ad2=ad2, ad3=ad3)       
    
    
    @app.route('/location_search')
    def location_search():
        """
        Allows user to search by map for a facility. 
        """
        return render_template('index.html')
    
    @app.route('/report', methods = ['GET', 'POST'])
    def report():
        """ 
        Returns report on facility.
        """
        facility_name=request.args.get('facility_name')
        if request.method == "POST":
            name=request.args.get('facility_name')
        a = query_report(facility_name)
        number_of_expected_filings=a[0]
        sub = a[1]
        return render_template('report.html', 
                               facility_name = facility_name, 
                               number_of_expected_filings = number_of_expected_filings,
                               sub = sub)
    
    
    return app