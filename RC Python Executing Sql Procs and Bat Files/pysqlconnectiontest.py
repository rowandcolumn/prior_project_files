import pyodbc # for calling sqlserver
import subprocess # for calling bat files
import time # for wait period between execution of procs and bat file execution

# Connection to MSSQL
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PGH;'
                      'Database=Northwind;'
                      'Trusted_Connection=yes;')
# Create Cursor
cursor = conn.cursor()
for row in cursor:
    print(row)
