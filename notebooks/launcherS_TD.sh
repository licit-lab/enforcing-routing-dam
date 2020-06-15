#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Test Sensitivity Td

# Scenario A 

case="PD"
kp=0.6
distance=600

for k in 100 200 250 300 350 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNAK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNAK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNAK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNAK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &    
done

echo "Total Simulations: ${IT}"

# Scenario B

for k in 100 200 250 300 350 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNBK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNBK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNBK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNBK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &   
done

# Scenario C

for k in 100 200 250 300 350 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNCK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNCK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_C.xml" \
    -p DEMAND_FILE "demand_scenario_C.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNCK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNCK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_C.xml" \
    -p DEMAND_FILE "demand_scenario_C.csv" &
done

echo "Total Simulations: ${IT}"