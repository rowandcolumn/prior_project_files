#====================================================
#---------- PYTHON EXCEL MACRO SCRIPT v5 ------------
#====================================================

#===== REQUIRED PYTHON MODULES ======================
# Python 3.7
import xlwings as xw
from pathlib import Path

#===== INPUTS =======================================
wd = Path() # Sets working directory based on current path using Pathlib module
filenamesearch = str(input('Type YYYYMM of period being reported: '))
resultingquery = '**/*' + str(filenamesearch) + '.xlsx' # Sets up the path and filename to look for based on above input
macro_name = "'PERSONAL.XLSB'!DivisionalReport" # Change this to your saved macro name you want to run

#===== CREATES AUDIT CSV FILE ======================
f = open('AuditReport_' + str(filenamesearch) + '.csv','w+')
f.write('Filename,')
f.write('BUD CM NOI,')
f.write('T3M AVG CM NOI,')
f.write('ERROR' + '\n')

#===== APPLIES EXCEL MACROS =========================
for item in wd.glob(resultingquery):
    try:
        print(str(item))
        wb = xw.Book(str(item))
        app = wb.app
        macro_vba = app.macro(macro_name) 
        macro_vba()
        try:
            sht = wb.sheets['Finance Review 3']
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
