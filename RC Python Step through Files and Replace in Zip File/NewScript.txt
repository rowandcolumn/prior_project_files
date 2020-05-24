# LIBRARY/MODULE IMPORT
import patoolib # You may have to use pipinstall to install the patoolib library.
import fnmatch # You may have to use pipinstall to install the patoolib library.
import os
import sys
import time

# SETS FIND AND REPLACE VARIABLES
search_term = "PutTheSearchTermHere"
replacement = "PutTheReplacementTermHere"

# get path of folder holding the program
scrptPth = os.path.dirname(os.path.realpath(__file__)) # Maybe finds the true path for the object File which is the file currently executing (i.e. the python script here)).

# SETS WORKING DIRECTORY
rootdir = "C:\\Users\Peter\Python Scripts 2017\Dad\CurrentTest" # Note the '//' after C:
os.chdir(rootdir) # Changes Directory to working directory

#LISTS THE FILES IN THE CURRENT DIRECTORY (NON ESSENTIAL)
print('Folders in New Root Directory:', os.listdir())

for filename in os.listdir():								# for each file 
    xlsx_file, ext = os.path.splitext(filename)
    if ext == ".xlsx":										# if it is a .xlsx 
        os.rename(xlsx_file + ".xlsx", xlsx_file + ".zip") 		# Renames as a zip
		try:
			patoolib.extract_archive(xlsx_file + ".zip") 			# Unarchives the Newly Reclassified Zip File
			os.chdir(xlsx_file) 									# Changes Directory to unziped folder
			for root, dirs, files in os.walk("."):  				# walk through the current folder & subfolders
				for filename in files:									# for each file, ...
					xml_file, ext = os.path.splitext(filename) 			# get its name
					if ext == ".xml":									# if an .XML  												
						os.rename(xml_file + ".xml", xml_file + ".txt") 	# Rename it to .txt
						try:
							with open(xml_file + ".txt") as f:	
								s = f.read()									# Read in its contents
								s = s.replace(search_term, replacement)			# do the replace
							with open(xml_file + ".txt", "w") as f:
								f.write(s)										# write replaced contents
						except:
							print "Replace failed for " + xml_file + ".xml"
						os.rename(xml_file + ".txt",xml_file + ".xml") 		# Rename it back to original name
			os.chdir("..") 											# Changes Directory to originalfolder
			os.remove(xlsx_file + ".zip") 							# DEletes the original Zip File
			patool create # /path/to/myfiles.zip file1.txt dir/		# RE-ARCHIVES/RE-ZIPS 
		except:
			print "xlsx_file + ".xlsx Failed to unzip"
        os.rename(xlsx_file + ".zip", xlsx_file + ".xlsx") 		# Renames zip back to .xlsx

