#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Sensitivity Beta - Cooperative 3: 

# Scenario A

case="COPNL"

for k in 0.1 0.2 0.3 0.4 0.5
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_BETA_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNABETA_${k} \
    -p CTR_ALG ${case} \
    -p BETA ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_BETA_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNABETA_${k} \
    -p CTR_ALG ${case} \
    -p BETA ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &    
done

echo "Total Simulations: ${IT}"