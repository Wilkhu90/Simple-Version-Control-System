#!/bin/bash
##Shell Script to run the python program if the file *.txt is opened in the specific path i.e. /Deskptop/*

result=$(ps -ef|grep gedit|grep Desktop/pyfiles)
filein=$(ps -ef|grep gedit|grep Desktop/pyfiles|cut -d'/' -f6) 
verify=$(tail -1 FileLog.txt)

if  [ "$result" ]; then
nohup ./VersionControl.py $filein $verify &
echo $filein >> FileLog.txt
else
echo "Nothing to be created."
fi
exit 0
