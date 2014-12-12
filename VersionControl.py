#!/usr/bin/python3.3
##Version Control System which will contol versioning 
##of files everytime they are open and something written to it.

##Created By: Sumeet WIlkhu
##Created On: 9th December, 2014
##Created for: Personal Use
##If found using this code without reference, it would be counted as plagiarism.
##Ok, let's Start!

##set a directory in which files are created and stored..The program is assumed to be up and running using nohup.
##Once the file from the designated folder is opened, the program is suppose to save a fresh copy in order to mantain an order or version.
##As soon as you open a file which doesn't exist in the folder of been created for the first time, it should better exist.
##Once we have the first copy, keep track if the file is appended. IF yes then create a +1 version of it. Else leave it as it is.
##

import sys
import os
import fnmatch
##File is path for file. Not a file itself.

##def CheckWhichFile():
##	return file1


def VersionControl(file1):
	if file1:
		tempfile=str(file1)
		filename,extension=tempfile.split('.')

		infile = open(file1, 'r')
		files=[]
		for filecount in os.listdir('.'):
			if fnmatch.fnmatch(filecount, filename+'*.'+extension):
				files.append(filecount)
		Newf,Newex=files[-1].split('.')
		if Newf[-1].isdigit():
			counter=int(Newf[-1])+1
			outfile=open(Newf[:-1]+str(counter)+'.'+Newex,'a')
		else:
			outfile=open(filename+'1.'+extension,'a')
				
		for line in infile.readlines():
  			outfile.write(line)

		infile.close()
		outfile.close()

filein=str(sys.argv[1])
verify=str(sys.argv[2])
print(filein)
print(verify)

##filein=CheckWhichFile()
if filein!=verify:
    	VersionControl(filein)
else:
	print('Nothing happened')
