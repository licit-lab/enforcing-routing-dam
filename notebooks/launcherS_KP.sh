#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Sensitivity Kp: 

# Scenario A 

case="P"

for k in  0.01 0.05 0.1 0.15 0.2
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNAKP_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNAKP_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &    
done

# Scenario B

for k in  0.01 0.05 0.1 0.15 0.2
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_dB.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNBKP_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p FILE "manhattan_grid_5X5_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_dB.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNBKP_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p FILE "manhattan_grid_5X5_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &    
done

echo "Total Simulations: ${IT}"