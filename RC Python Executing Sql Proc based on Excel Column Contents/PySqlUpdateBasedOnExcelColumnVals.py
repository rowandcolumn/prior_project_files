#====================================================
#---------- PYTHON EXCEL UPDATE SCRIPT v1 ------------
#====================================================

#===== REQUIRED PYTHON MODULES ======================
# Python 3.7
import xlwings as xw
from pathlib import Path
import pyodbc # for calling sqlserver
import subprocess # for calling bat files
import time # for wait period between execution of procs and bat file execution

#===== INPUTS =======================================
wd = Path() # Sets working directory based on current path using Pathlib module
filenamesearch = str(input('Excel File Name NO EXTENSION: '))
resultingquery = '**/*' + str(filenamesearch) + '.xlsx' # Sets up the path and filename to look for based on above input
excelSheetName = '5.Non Labor'
sqldbName = ''
sqlTableName = ''

# SQL SERVER CONNECTIONS (ONE FOR EACH DB) - AUTOCOMMIT MUST BE SET TO TRUE IF YOU WANT TO WRITE PERM
conn_OSR_Repository_String = 'Driver={SQL Server};''Server=PGH;''Database=OSR_Repository;''Trusted_Connection=YES;'
conn_OSR_Repository = pyodbc.connect(conn_OSR_Repository_String, autocommit=True)

# CREATION OF TWO SQL SERVER CURSORS
cursor_OSR = conn_OSR_Repository.cursor()

#===== APPLIES EXCEL MACROS =========================
for item in wd.glob(resultingquery):
    try:
        wb = xw.Book(str(item))
        app = wb.app
        try:
            sht = wb.sheets[excelSheetName]
            f.write(str(item) + ",")
            f.write(str(sht.range('f62').value) + ',')
            f.write(str(sht.range('j62').value) + ',')
            f.write(str(sht.range('z62').value) + '\n')
            # f.write('-------------------------------------------------' + '\n')
            print(str(item) + '  ' + str(sht.range('f62').value) + '  ' + str(sht.range('j62').value) + '  ' + str(sht.range('z62').value))
        except:
            f.write('Error Occured ' + '\n')
        wb.close()
        app.quit()
        app.kill()
    except:
        Print('Error Occured  ')
        #wb.close()
        app.quit()
        app.kill()
    
#===== SCRIPT CLEANUP ======================
f.close()
print('----- Script Completed -----')

# SETS QUERY TO GET DIVISION CODES FROM DBO.D_DIVISION VIEW WHERE OPCO
query_division = "INSERT INTO {} "

# CURSOR QUERIES DIVISION CODES FROM DBO.D_DIVISION VIEW WHERE OPCO
cursor_BI360.execute(query_division)

# ROWS VARIABLE CAPTURES ALL DIVISION CODES TO ITERATE THROUGH
# POTENTIAL PROBLEM: THIS CAN CASE ISSUES AS IT RETURNS A DICTIONARY, NOT A STRING
rows = cursor_BI360.fetchall()

# LOOPS THROUGH ROWS DICTIONARY EXECUTING TWO SQL PROCS TO UPDATE SUBSCRIBER AND SUBSCRIPTION
for row in rows:
    # print(row[0]) # Prints the query result without the corresponding key since the returned data type is a dictionary
    proc_Update_Subscriber = 'Exec Change_Subscriber @user_name = "' + record_To_Alter + '", @new_Dir = "' + str(row) + '"'
    proc_Update_Subscription = 'Exec Change_Subscription @user_name = "' + record_To_Alter + '", @new_parameter_name_division = "' + str(row) + '"'
    cursor_OSR.execute(proc_Update_Subscriber)
    cursor_OSR.execute(proc_Update_Subscription)
print('Update Procs Completed')

# CLOSES ALL CONNECTIONS AND CURSORS
cursor_BI360.close()
cursor_OSR.close()
conn_OSR_Repository.close()
conn_BI360DW_VillaHC.close()

# WAIT FOR PROCS TO EXECUTE BEFORE CALLING BAT FILE/S
time.sleep(10) # Seconds

# BAT FILE EXECUTION
subprocess.call(['C:\\Users\\Peter\\Desktop\\Row & Column Project\\test.bat'])