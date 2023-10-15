#!/usr/bin/bash

NONE -m &> error.txt
echo "-----See exit code below-----"
echo "Exit code: $?"

ls > out.txt
echo "-----See exit code below-----"
echo "Exit code: $?"

#exit code is $?
#just have to echo it like below
#echo $?

