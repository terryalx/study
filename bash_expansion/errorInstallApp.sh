#!/usr/bin/bash

prog=DOESNOTEXIST

if command -v $prog
then
	echo "$prog is installed"
	echo "Run an update...."
else
	echo "$prog is not installed"
	echo "Installing..."
	#sudo apt update && sudo install -y $prog
fi

if [ $? -eq 0 ]
then
	echo "Successful.."
else
	echo "Failed.."
	echo "Do Something i.e send an email to SRE"
fi

