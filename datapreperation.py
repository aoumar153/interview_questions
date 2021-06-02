# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:13:56 2021

@author: abdul
"""
import pandas as pd
import numpy as np
data = pd.read_csv(r'C:\Users\abdul\Downloads\2017.csv')

data.shape
#got rid of salaries of 0 and duplicates in data
data.drop_duplicates(inplace = True)
data.drop(data.index[data['SALARY'] == '$0.00'], inplace = True)


data['POSITION TITLE'] = data['POSITION TITLE'].fillna(0)
#data["POSITION TITLE"] = data["PAY BASIS"].apply(lambda x: x.split(' ', ) if x == type(int))

#print('IT is ',data['POSITION TITLE'].dtypes)


#cleaning up salaries 

s = data['SALARY'].apply(lambda x: int(float(x.replace('$','').replace(',','')) ))

#feature engineering (looking through position title for any significant titles )
data['president_help'] = data['POSITION TITLE'].apply(lambda x: 1 if 'to the president' in str(x).lower() else 0)
data['seniority'] = data['POSITION TITLE'].apply(lambda x: 1 if 'senior' in str(x).lower() else 0)
data['director_of'] = data['POSITION TITLE'].apply(lambda x: 1 if 'director of' in str(x).lower() else 0)
data['director_for'] = data['POSITION TITLE'].apply(lambda x: 1 if 'director for' in str(x).lower() else 0)
data['special'] = data['POSITION TITLE'].apply(lambda x: 1 if 'special' in str(x).lower() else 0)
data['chief'] = data['POSITION TITLE'].apply(lambda x: 1 if 'chief' in str(x).lower() else 0)
data['presidential'] = data['POSITION TITLE'].apply(lambda x: 1 if 'presidential personnel' in str(x).lower() else 0)

