#!/usr/bin/env python

import sqlite3
import csv
import os

#initialize and connect to SQL lite db

db_name = "diamonds"

def createDatabase(db_name):
    
    con = sqlite3.connect(db_name)

    with con:
        
        cur = con.cursor()
        cur.execute("CREATE TABLE diamonds(carat TEXT, cut TEXT, color TEXT, clarity TEXT, depth TEXT, price TEXT)")


#read .csv file, creating a new line in the db with each line of the csv

def readCSV(db_name):
    
    filename = "diamonds.csv"
   
    with open(filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        
              
    con = sqlite3.connect(db_name)

    with con:
        cur = con.cursor()
        for row in reader:
            


#prompt user for two db parameters

def userPromptCut():
    param1 = input("What cut shall I query the diamonds database for? [Ideal, Premium, Very Good, Good, Fair]")
    #validate for cut, must match valid category

    if param1 == "Ideal":
        return param1
    elif param1 == "Premium":
        return param1
    elif param1 == "Very Good":
        return param1
    elif param1 == "Good":
        return param1
    elif param == "Fair":
        return param1
    else:
        return "Ideal"
    
def userPromptCarat(max_carat):    
    param2 = input("And what carat shall I query the diamonds database for? Please enter a number with two decimal places")
    param2 = float(param2)

    #use the largest polished diamond ever as a max instead of the table limit
    if 235 > param2 > 0:
         return param2
    else:
        return float(3.3)




#validate entries

def validate(param1, param2):

    

#query db with valid entries

def query(param1, param2):


#print output


                       


create_db(db_name)

