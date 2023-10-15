#!/usr/bin/bash

#if statement
#if condition -> then do_something_like echo -> fi to_end_or_close_the_if_statement

my_num=100

#-------------------->test1<-------------------------

if [ $my_num -eq 100 ]
then
	echo "My num is $my_num True"
fi

#-------------------->test2<-------------------------

if [ $my_num -eq 100 ]
then
	echo "True $my_num"
else
	echo "False $my_num"
fi

#-------------------->test3<-------------------------

if [ ! $my_num -eq 300 ]
then    
	echo "True $my_num"
else    
	echo "False $my_num"
fi

#-------------------->test4<-------------------------

if [ $my_num -ne 300 ]
then
	echo "NOT"
else
	echo "YES"
fi



#-eq ---> equal
#-ne ---> not equal
#-gt ---> greater than


#---------Check if file exist in a path

if [ -f ~/myfile.txt ]
then
	echo "File exists"
else
	echo "File does not exist"
fi


