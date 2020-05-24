# REQUIREMENTS
import pyodbc # for calling sqlserver
import subprocess # for calling bat files
import time # for wait period between execution of procs and bat file execution

# CONNECTS TO MSSQL DATABASE
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PGH;'
                      'Database=OSR_Repository;'
                      'Trusted_Connection=YES;')

# CREATES SQL CURSOR
cursor = conn.cursor()

# TEST INPUTS
theUserName = '2001'
querySelect = "Select data from Subscribers where Name = N'2001'"
procChangeSubscription = "Exec Change_Subscription @user_name = N'2001', @name_replacement = 'Name Replacement', @new_document = 'New Directory', @new_parameter_name_division = 'New Parameter Name Division', @new_parameter_name_period = 'New Parameter Name Period'"
procChangeSubscriber = "Exec SubscriberChange @user_name = N'2001', @new_Email = 'Peter@testdata.com', @new_Dir = 'Dir'"

# EXECUTES QUERY OR PROC IN SQL SERVER
cursor.execute(querySelect)
# cursor.execute(procChangeSubscription)
# cursor.execute(procChangeSubscriber)

# PRINTS RESULTS OF **CURRENT** QUERY LAST EXECUTED
for row in cursor:
    print(row)

# WAIT FOR PROCS TO EXECUTE BEFORE CALLING BAT FILE/S
time.sleep(10) # Seconds

# BAT FILE EXECUTION
subprocess.call(['C:\\Users\\Peter\\Desktop\\Row & Column Project\\test.bat'])
