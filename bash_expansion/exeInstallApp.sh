#!/usr/bin/bash

#checking if a prog is installed and if not install it...

prog=/usr/bin/htop

echo "----------test example----------"
#test command style
if [ -f $prog ]
then
	echo "$prog is available"
	echo "Display version and details"
else
	echo "$prog is not available"
	echo "Update this code to run and install $prog"
fi

#----------run--------------
#$prog

#check for all prog..
#check for updates
#check for all updates and update


echo "----------command example---------"
#command command style
if command -v $command
then
	echo "Yes $command"
else
	echo "No $command"
fi

