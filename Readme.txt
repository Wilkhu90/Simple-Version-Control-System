The following Readme.txt file is intended to clear the prequisites required before you start using the
Simple Version Control System. You need to follow these steps in order to setup the VC system.

1) Copy the essential files (ShellBot.sh, VersionControl.py & FileLog.txt) in any folder you desire to which the VC rules to be applied. The directory in which these files exist will become the directory in which the VC will work. Anything opened from outside the specified directory will have no affect on VC system.

2) As soon as you copy the essential files in a directory, add the same directory into the code of ShellBot.sh.

3) Create a crontab entry in your linux system by using (crontab -e) and add the following lines 
(* * * * * cd Desktop/pyfiles; ./ShellBot.sh) without the brackets at the end of the crontab.

4) If every change happened succesfully, the VC system should be working now.

P.S. Make sure to check for permissions of essential files. The minimum should be 755.

Regards,
Sumeet Wilkhu
