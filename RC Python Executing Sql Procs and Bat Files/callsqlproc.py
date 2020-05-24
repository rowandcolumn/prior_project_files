import pyodbc # for calling sqlserver
import subprocess # for calling bat files
import time # for wait period between execution of procs and bat file execution

# Connection to MSSQL
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-SAI3SC3;'
                      'Database=Northwind;'
                      'Trusted_Connection=yes;')
# Create Cursor
cursor = conn.cursor()

# Parameter Inputs
username = ""
nameReplacement = ""
newDocument = ""
newParameterNameDivision = ""
newParameterNameDivision = ""
newEmail = ""

# Procedure Statements
change_Subscription = "Exec Change_Subscription @user_name = N'2001', @name_replacement = 'Name Replacement', @new_document = 'New Directory', @new_parameter_name_division = 'New Parameter Name Division', @new_parameter_name_period = 'New Parameter Name Period'"

change_Subscriber = "Exec SubscriberChange @user_name = N'2001', @new_Email = 'Peter@testdata.com', @new_Dir = 'Dir'"
# Cursor Execution of Query to MSSQL
cursor.execute(change_Subscription)
cursor.execute(change_Subscriber)
# Print Query results to Terminal
for row in cursor:
    print(row)

# Wait for procs to execute before calling bat file
time.sleep(10) # Seconds

# Bat file execution following Prod execution
subprocess.call(['C:\\Users\\Peter\\Desktop\\Row & Column Project\\test.bat'])