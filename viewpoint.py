# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 02:47:17 2021

@author: abdul
"""

import pandas as pd

def up (x):
    con = 'e'
    #c = 'E'
    b = 'b'
    #s = 'B'    
    if con in x:
        return x.upper()
    elif b in x:
        return x.lower()
    else : return x
 

       
name_table = pd.DataFrame({'StudentID':['V001','V002','V003','V004'], 'Names':['Abe','Abhay','Acelin','Adelphos']})

mark_table = pd.DataFrame({'StudentID':['V001','V002','V003','V004'], 'Total_marks':[95,80,74,81]})

name_table['Names'] = name_table['Names'].apply(up)



def dfnew():   
    
    df_inner = pd.merge(mark_table , name_table, on='StudentID', how='inner')

    rslt_df = df_inner[df_inner['Names'].str.isupper()] 
    rslt_df2 = df_inner[df_inner['Names'].str.islower()] 

    mean2 = rslt_df['Total_marks'].mean()
    mean1 = rslt_df2['Total_marks'].mean()
    
    avg = pd.DataFrame({'Uppercase E':[mean2],'Lowercase b':mean1})
    print(avg)  

dfnew()
