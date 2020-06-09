#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Test Sensitivity Td

# Scenario A 

case="PD"

for k in 200 250 300 350 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNAK05D800.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNAK05D800_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.5 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNAK05D800.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNAK05D800_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.5 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &    
done

echo "Total Simulations: ${IT}"

# Scenario B

case="PD"

for k in 200 250 300 350 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNBK05D800.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNBK05D800_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.5 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNBK05D800.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNBK05D800_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.5 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &   
done

echo "Total Simulations: ${IT}"