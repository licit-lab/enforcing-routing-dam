#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"

for case in CO_P CO_PI P PI OPENL
do
   if [ "$case" == "OL" ]; then 
        papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
   -p PATH_SYMUVIA ${PATH_SYMUVIA} -p CONTROL_TYPE ${case} &
   else
       papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
   -p CASE ${case} -p PATH_SYMUVIA ${PATH_SYMUVIA} &
   fi
done