#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Sensitivity Beta - Cooperative 3: 

# Scenario A

case="COSTN3"

kp=0.65
td=0.0
distance=800

for k in 0.05 0.1 0.15 0.20 0.25 0.3 0.35 0.4 0.45
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_BETA_${k}_SCNAD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_0.5_X_X_${k} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p BETA ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))    
    papermill 01_Zone_Control.ipynb 01_Zone_Control_BETA_${k}_SCNAD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_0.5_X_X_${k} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p BETA ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &   
done

# Scenario B

kp=0.65
td=0.0
distance=600

for k in 0.05 0.1 0.15 0.20 0.25 0.3 0.35 0.4 0.45
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_BETA_${k}_SCNBD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_0.5_X_X_${k} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p BETA ${k} \    
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_BETA_${k}_SCNBD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_0.5_X_X_${k} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p BETA ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &    
done


echo "Total Simulations: ${IT}"