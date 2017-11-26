"""
Data Mining 2017 Fall
HW1: Python Practice
"""

## Necessary libraries
import pandas as pd
import numpy as np
import math

def dataclean(data):
    ## remove columns
    data = data.drop(['Ticket','Name'],axis=1)
    
    ## if null then fill 0
    data.Sex.fillna('0', inplace=True)
    data.Cabin.fillna('0', inplace=True)
    data.Embarked.fillna('0', inplace=True)
    
    ## remove null rows
    data = data.dropna()
    
    ## fix age
    data["Age"] = (data["Age"]+0.6).apply(np.fix).apply(np.int)
    
    ## data transfer
    data.loc[data.Sex == 'male', 'Sex'] = 1
    data.loc[data.Sex == 'female', 'Sex'] = 0
    data.loc[data.Embarked == 'C', 'Embarked'] = 1
    data.loc[data.Embarked == 'Q', 'Embarked'] = 2
    data.loc[data.Embarked == 'S', 'Embarked'] = 3
    data.loc[data.Cabin.str[0] == 'A', 'Cabin'] = 1
    data.loc[data.Cabin.str[0] == 'B', 'Cabin'] = 2
    data.loc[data.Cabin.str[0] == 'C', 'Cabin'] = 3
    data.loc[data.Cabin.str[0] == 'D', 'Cabin'] = 4
    data.loc[data.Cabin.str[0] == 'E', 'Cabin'] = 5
    data.loc[data.Cabin.str[0] == 'F', 'Cabin'] = 6
    data.loc[data.Cabin.str[0] == 'G', 'Cabin'] = 7
    data.loc[data.Cabin.str[0] == 'T', 'Cabin'] = 8
            
    return data

if __name__ == "__main__":
    ## import train data
    train_data = pd.read_csv('train.csv', index_col='PassengerId')
    
    train_data = dataclean(train_data)
    
    ## sort
    train_data = train_data.sort_values(by = "Age")
    
    print train_data
    

