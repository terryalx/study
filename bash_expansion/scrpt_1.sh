#!/bin/bash

echo "Hello Efe..bash scripting!"

#variables -> store items to use later
#must use "" to reference variable

name="Terry"
echo $name

#save variable
#subshell-> $()
#subshell executes commands in the background and store it

my_bin=$(ls /bin | grep server)
echo $my_bin

my_pwd=$(pwd)
echo $my_pwd

#show all system decleared variable
env

