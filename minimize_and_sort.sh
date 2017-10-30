#!/bin/bash

if [[ $# -ne 2 ]]; then

	echo "Illegal number of parameters";
	exit 1

else
	
	echo $1 $2;
	awk -F ";" '{printf "%s;%s;%s\n",$2,$8,$9}' $1 | sort -S 100000000 -t';' -k2 - > $2;
 
fi


