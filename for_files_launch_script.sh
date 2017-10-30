#!/bin/bash

f_list=($(ls motionl_MT_ngprs_T*))

for i in "${f_list[@]}"; do

	printf $i"_sorted_4\n";
	./minimize_and_sort.sh $i $i"_sorted_4";	

done
