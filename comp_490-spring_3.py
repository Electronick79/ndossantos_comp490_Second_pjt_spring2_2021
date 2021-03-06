import sqlite3

import mysql as mysql
import pandas as pd

# template that you can use to connect Python to SQL Server
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=database_name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM database_name.table')

for row in cursor:
    print(row)

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
  )
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()

# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE comp490_spring_3")

# get list of all databases
db_cursor.execute("SHOW DATABASES")

#print all databases
for db in db_cursor:
    print(db)

df = pd.read_csv(r'Path where the XLSX file is stored\COMP490_SPRING_3.XLSX')
print(df)

df = pd.read_csv(r'C:\Users\Electronick\OneDrive\Desktop\COMP_490\COMP490_SPRING_3.xlsx')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\').

print(df)

conn = sqlite3.connect('TestDB.db')
c = conn.cursor()

# Create table - occupation occupational
c.execute('''CREATE TABLE OCCUPATIONAL
             ([generated_id] INTEGER PRIMARY KEY,[Occupational_Name] text, [Title] text, [Date_start] dates, [Occupation] occupation, [Wage] integer, [State] text,,)''')

db_cursor.execute("SHOW TABLES")
for table in db_cursor:
    print(table)

# Create table - STATES
c.execute('''CREATE TABLE STATES
             ([generated_id] INTEGER PRIMARY KEY,[States_ID] integer, [States_Name] text)''')

db_cursor.execute("SHOW TABLES")
for table in db_cursor:
    print(table)

# Create table - EMPLOYMENT
c.execute('''CREATE TABLE EMPLOYMENT_STATUS
             ([Employment_Name] text, [STATE_Name] text, [Date] date), [ Field_in_that_state] text''')
db_cursor.execute("SHOW TABLES")

for table in db_cursor:
    print(table)

# Create table - 25TH_PERCENTILE_SALARY
c.execute('''CREATE TABLE 25TH_PERCENTILE_SALARY
             ([25th_percent_salary] integer, [Employment_Name] text, [Date] date), [ Field_in_that_state] text''')

db_cursor.execute("SHOW TABLES")
for table in db_cursor:
    print(table)


conn.commit()



