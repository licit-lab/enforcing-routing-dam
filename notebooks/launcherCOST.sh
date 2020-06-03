#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Test 3 cooperative strategies 

# Scenario A

for case in COST1 COST2 COST3
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNACOST_${case} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.7 \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))    
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNACOST_${case} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.7 \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &     
done  

echo "Total Simulations: ${IT}"