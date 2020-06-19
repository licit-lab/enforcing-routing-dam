#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Sensitivity Alpha - Cooperative 7: 

# Scenario A

case="COSTN7"

kp=0.65
td=0.0
distance=800

for k in 0.1 0.2 0.3 0.4 0.5 0.6
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_COKP_${k}_SCNAD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_X_${k}_X_X \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p CO_KP ${k} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))    
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_COKP_${k}_SCNAD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_X_${k}_X_X \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p CO_KP ${k} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" & 
done

# Scenario B

kp=0.65
td=0.0
distance=600

for k in 0.1 0.2 0.3 0.4 0.5 0.6
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_COKP_${k}_SCNBD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_X_${k}_X_X \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p CO_KP ${k} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_COKP_${k}_SCNBD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_X_${k}_X_X \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p CO_KP ${k} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" & 
done


echo "Total Simulations: ${IT}"