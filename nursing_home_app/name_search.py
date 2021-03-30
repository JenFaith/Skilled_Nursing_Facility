# Basic Packages
import numpy as np
import pandas as pd
import re
import sqlite3

# Modeling
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def return_similar(user_type, sql_name='nhs_descriptions.sqlite3'):
    # connect to database and pull df
    con = sqlite3.connect(sql_name)
    df = pd.read_sql_query("SELECT * FROM Data", con)
    
    # assign already existing values to lists
    corpus = df['provider_name'].to_list()
    number = df['federal_provider_number'].to_list()
    
    # insert user values
    corpus.insert(0, user_type)
    number.insert(0, "user_input")
    
    # clean text
    for i in range(len(corpus)):
        corpus[i] = corpus[i].lower()
        corpus[i] = re.sub('[^a-z ]','', corpus[i])
    
    # vectorize
    vectorizer = TfidfVectorizer(analyzer='char')
    trsfm=vectorizer.fit_transform(corpus)
    vect = pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names(), index = number)
    similar_score = cosine_similarity(trsfm[0:1], trsfm)
    vect['score']= np.array(similar_score[0])
    vect = vect.sort_values(by = 'score', ascending = False).reset_index()
    num1 = df[df['federal_provider_number']==(vect['index'][1])]['federal_provider_number'].values[0]
    num2 = df[df['federal_provider_number']==(vect['index'][2])]['federal_provider_number'].values[0]
    num3 = df[df['federal_provider_number']==(vect['index'][3])]['federal_provider_number'].values[0]
    name1 = df[df['federal_provider_number']==num1]['provider_name'].values[0]
    name2 = df[df['federal_provider_number']==num2]['provider_name'].values[0]
    name3 = df[df['federal_provider_number']==num3]['provider_name'].values[0]
    ad1 = df[df['federal_provider_number']==num1]['full_address'].values[0]
    ad2 = df[df['federal_provider_number']==num2]['full_address'].values[0]
    ad3 = df[df['federal_provider_number']==num3]['full_address'].values[0]
    return num1, num2, num3, name1, name2, name3, ad1, ad2, ad3

# num1, num2, num3, name1, name2, name3, ad1, ad2, ad3 = return_similar('seeson carecenter')
# print(name1)