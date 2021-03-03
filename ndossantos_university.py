import mysql.connector
import mysql.connector


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")


    return connection
connection = create_server_connection("localhost", "root", pw)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

mycursor.excute("CREATE TABLE studentschool((200),(3),(48),"
                "(),(),"
                "2016.repayment.3_yr_repayment.overall()")
for tb in mycursor:
     create_school.name = """
    CREATE TABLE school.name (
      school.name INT PRIMARY KEY,
      school.name VARCHAR(40) NOT NULL,
      address VARCHAR(60) NOT NULL,
      school.name VARCHAR(20)
    );
     """
     create_school.city = """
     CREATE TABLE school.city (
       school.city_id INT PRIMARY KEY,
       school.city VARCHAR(40) NOT NULL,
       school.city VARCHAR(40) NOT NULL,
       school.city_phone VARCHAR(6),
       school.city INT
     );
     """
     create_2020.student.size = """
     CREATE TABLE 2020.student.size (
       2020.student.size INT PRIMARY KEY,
       2020.student.size VARCHAR(40) NOT NULL,
       020.student.size VARCHAR(3) NOT NULL,
       level VARCHAR(2),
       2020.student.size INT,
       
     );
     """
     create_2018student.size = """
          CREATE TABLE 2018student.size (
            2018student.size_id INT PRIMARY KEY,
            2018student.size VARCHAR(40) NOT NULL,
            2018student.size VARCHAR(40) NOT NULL,
            
          );
          """
     create_2017.earnings_3_yrs_after_completion.overall_count_over_poverty_line= """
        CREATE TABLE 2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line (
          2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line INT PRIMARY KEY,
          2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line VARCHAR(40) NOT NULL,
          2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line VARCHAR(20)
        );
         """
     create_2016.repayment_3_yr_repayment.overall = """
          CREATE TABLE 2016.repayment.3_yr_repayment.overall (
            2016.repayment.3_yr_repayment.overall INT PRIMARY KEY,
            2016.repayment.3_yr_repayment.overall VARCHAR(40) NOT NULL,
            2016.repayment.3_yr_repayment.overall VARCHAR(40) NOT NULL,
            
          );
          """
     connection = create_db_connection("localhost", "root", pw, db)
     execute_query(connection, create_school.name)
     execute_query(connection, create_school.city)
     execute_query(connection, create_2020.student.size)

     execute_query(connection, create_2018student.size)
     execute_query(connection, create_2017.earnings_3_yrs_after_completion.overall_count_over_poverty_line)
     execute_query(connection, create_2016.repayment_3_yr_repayment.overall)
