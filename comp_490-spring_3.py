import sqlite3
import pandas as pd
#import openpyxl

df = pd.read_csv(r'Path where the CSV file is stored\COMP490_SPRING_3.XLSX')
print (df)


conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

# Create table - occupation occupational
c.execute('''CREATE TABLE OCCUPATIONAL
             ([generated_id] INTEGER PRIMARY KEY,[Occupational_Name] text, [Title] text, [Date_start] dates, [Occupation] occupation, [Wage] integer, [State] text,,)''')

# Create table - STATES
c.execute('''CREATE TABLE STATES
             ([generated_id] INTEGER PRIMARY KEY,[States_ID] integer, [States_Name] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE DAILY_STATUS
             ([Client_Name] text, [Country_Name] text, [Date] date)''')

conn.commit()






#df = pd.DataFrame({'States':['California', 'Florida', 'Montana', 'Colorodo', 'Washington', 'Virginia'],
   # 'Capitals':['Sacramento', 'Tallahassee', 'Helena', 'Denver', 'Olympia', 'Richmond'],
    #'Population':['508529', '193551', '32315', '619968', '52555', '227032']})
