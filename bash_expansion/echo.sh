#!/usr/bin/bash

c1=ls
c2=lr

$c1
if command -v $c1
then
	echo "$c1"
else
	echo "Unknown"
fi

