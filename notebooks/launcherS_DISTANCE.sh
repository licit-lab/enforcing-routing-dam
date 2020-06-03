#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Sensitivity Distance:

# Scenario A

case="P"

for k in 200 400 800 1200 1600
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_DST_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNADST_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p DISTANCE_CONTROL ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
     IT=$((IT+1))
     papermill 01_Zone_Control.ipynb 01_Zone_Control_DST_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNADST_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p DISTANCE_CONTROL ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &   
done

echo "Total Simulations: ${IT}"