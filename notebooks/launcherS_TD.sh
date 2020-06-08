#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Test Sensitivity Td

# Scenario A 

case="PD"

for k in 200 250 300 350 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNATD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.15 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNATD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.15 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &        
done

echo "Total Simulations: ${IT}"

# Scenario B

case="PD"

for k in 200 250 300 350 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_dB.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNATD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.15 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_dB.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNBTD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.15 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &       
done

echo "Total Simulations: ${IT}"