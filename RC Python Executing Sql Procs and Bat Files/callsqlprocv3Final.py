# REQUIREMENTS
import pyodbc # for calling sqlserver
import subprocess # for calling bat files
import time # for wait period between execution of procs and bat file execution

# SQL SERVER CONNECTIONS (ONE FOR EACH DB) - AUTOCOMMIT MUST BE SET TO TRUE IF YOU WANT TO WRITE PERM
conn_OSR_Repository_String = 'Driver={SQL Server};''Server=PGH;''Database=OSR_Repository;''Trusted_Connection=YES;'
conn_OSR_Repository = pyodbc.connect(conn_OSR_Repository_String, autocommit=True)

conn_BI360DW_VillaHC_String = 'Driver={SQL Server};''Server=PGH;''Database=BI360DW_VillaHC;''Trusted_Connection=YES;'
conn_BI360DW_VillaHC = pyodbc.connect(conn_BI360DW_VillaHC_String, autocommit=False)

# CREATION OF TWO SQL SERVER CURSORS
cursor_BI360 = conn_BI360DW_VillaHC.cursor()
cursor_OSR = conn_OSR_Repository.cursor()

# SETS RECORD TO ALTER IN SUBSCRIPTION AND SUBSCRIBER TABLE (SHOULD ONLY BE ONE)
record_To_Alter = '2002'

# SETS QUERY TO GET DIVISION CODES FROM DBO.D_DIVISION VIEW WHERE OPCO
query_division = "select code from dbo.d_Division where OpCo_PropCo = 'Opco'"

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