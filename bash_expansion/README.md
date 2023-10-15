######Bash Shell######

#show what shell your running?
echo $SHELL
which bash

man test
man command

#start using bash
usr/bin/bash

#variable -> store item for use
#$variable -> to print in the bash shell mode

#if statement
#By default the else statement executs if there is a mistake in the if block

#exit code
echo $?

#scripts run on a schedule
#you can have scripts running all night and wake up to check their esit code
#none 0 exit script means the script failed
#you can trigger non 0 exit code to do something
#like another script that emails the sysengr saying a script failed


#another use of exitcode is to force exit with a specific code so we write a script to check and track the code

