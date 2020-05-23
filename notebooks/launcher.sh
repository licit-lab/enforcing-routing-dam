#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"

for case in CO_P CO_PI P PI OPENL
do
   if [ "$case" == "OPENL" ]; then 
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p CTR_ALG ${case} \
    -p CONTROL_MODE ${case} &"
      papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p CTR_ALG ${case} \
    -p CONTROL_MODE ${case} &
   else
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p CTR_ALG ${case} &"
      papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p CTR_ALG ${case} &
   fi
done  


for case in CO_P CO_PI P PI OPENL
do
   if [ "$case" == "OPENL" ]; then 
   echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p CTR_ALG ${case} \
    -p CONTROL_MODE ${case} \
    -p FILE "symuvia_network_9zones.xml" \
    -p NRow 3 \
    -p NCol 3 \
    -p SCENARIO "mesh9x9/" \
    -p ZONES "9zones/" \
    -p REF_SPEED "ref_speeds_9zones.csv" &"
      papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p CTR_ALG ${case} \
    -p CONTROL_MODE ${case} \
    -p FILE "symuvia_network_9zones.xml" \
    -p NRow 3 \
    -p NCol 3 \
    -p SCENARIO "mesh9x9/" \
    -p ZONES "9zones/" \
    -p REF_SPEED "ref_speeds_9zones.csv" &
   else
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p CTR_ALG ${case} \
    -p FILE "symuvia_network_9zones.xml" \
    -p NRow 3 \
    -p NCol 3 \
    -p SCENARIO "mesh9x9/" \
    -p ZONES "9zones/" \
    -p REF_SPEED "ref_speeds_9zones.csv" &"
      papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p CTR_ALG ${case} \
    -p FILE "symuvia_network_9zones.xml" \
    -p NRow 3 \
    -p NCol 3 \
    -p SCENARIO "mesh9x9/" \
    -p ZONES "9zones/" \
    -p REF_SPEED "ref_speeds_9zones.csv" &
   fi
done