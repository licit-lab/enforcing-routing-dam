#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Test Sensitivity Td

# Scenario A 

case="PD"

for k in 100 200 300 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNATD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNATD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &        
done

echo "Total Simulations: ${IT}"