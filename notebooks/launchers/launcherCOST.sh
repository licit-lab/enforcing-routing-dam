#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Cooperative strategies 

# Scenario A
kp=0.65
td=0.0
distance=800

for case in COSTN1 COSTN2 COSTN3 COSTN4 COSTN5 COSTN6
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_SCNAD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_800_5X5_${case}_${kp}_${td}_0.5_${kp}_${td}_X \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))    
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_SCNAD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_800_5X5_${case}_${kp}_${td}_0.5_${kp}_${td}_X \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP ${kp} \
    -p CO_KP ${kp} \
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

for case in COSTN1 COSTN2 COSTN3 COSTN4 COSTN5 COSTN6
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_SCNBD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_800_5X5_${case}_${kp}_${td}_0.5_${kp}_${td}_X \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))    
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_SCNBD${distance}K${kp}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_800_5X5_${case}_${kp}_${td}_0.5_${kp}_${td}_X \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done  

echo "Total Simulations: ${IT}"