"""
Data Mining 2017 Fall
HW1: Python Practice
"""
import math
import csv
import re


#Show Data
def grades(file_path):
    read_file = open(file_path, 'r')
 
    #define each row name you want to use when read from .csv file
    reader=csv.DictReader(read_file, ["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket"])
    header=reader.fieldnames
    a_line_after_header = next(reader)
    
    a=()
    a=list(a)
    i=1
    showMax=100

    for row in reader:
        if (row['Name']<>"" and row['Pclass']<>""and row['Sex']<>""and row['Age']<>""and row['SibSp']<>""and row['Parch']<>""and i<=showMax):

            #Just show you want to see the data
            a.insert(0,(row['Age'],row['Name'],row['Pclass'],row['Sex'],row['SibSp'],row['Parch']))
            i=i+1
        

    read_file.close()

    #Sorted by x[0] means row['Age'], x[1] means row['Name']...etc
    test_array =sorted(a,key=lambda x:x[0])
 
    tuple_grades = list(test_array)

    return  tuple_grades



if __name__ == "__main__":
    pro_2_tuple = grades('train.csv')

    for x in range(1, 100):
        print (pro_2_tuple[x][0],pro_2_tuple[x][1],pro_2_tuple[x][2],pro_2_tuple[x][3],pro_2_tuple[x][4],pro_2_tuple[x][5])

