#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Sensitivity Kp: 

# Scenario A 

case="P"

# for k in 0.01 0.05 0.1 0.15 0.17 0.19 0.2 0.21 0.23 0.25 0.3 0.5
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNAD800.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNAD800_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${k} \
#     -p FILE "manhattan_grid_5X5_scenario_A.xml" \
#     -p DEMAND_FILE "demand_scenario_A.csv" &"
#     IT=$((IT+1))
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNAD800.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNAD800_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${k} \
#     -p FILE "manhattan_grid_5X5_scenario_A.xml" \
#     -p DEMAND_FILE "demand_scenario_A.csv" &
# done

# Scenario B

# for k in 0.01 0.05 0.1 0.15 0.17 0.19 0.2 0.21 0.23 0.25 0.3 0.5
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNBD800.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNBD800_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${k} \
#     -p FILE "manhattan_grid_5X5_B.xml" \
#     -p DEMAND_FILE "demand_scenario_B.csv" &"
#     IT=$((IT+1))
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNBD800.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNBD800_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${k} \
#     -p FILE "manhattan_grid_5X5_scenario_B.xml" \
#     -p DEMAND_FILE "demand_scenario_B.csv" &     
# done

# Scenario C

for k in  0.01 0.05 0.1 0.15 0.17 0.19 0.2 0.21 0.23 0.25 0.3 0.5
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNCD800.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT SKP_SCNCD800_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p FILE "manhattan_grid_5X5_C.xml" \
    -p DEMAND_FILE "demand_scenario_C.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNCD800.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT SKP_SCNCD800_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p FILE "manhattan_grid_5X5_C.xml" \
    -p DEMAND_FILE "demand_scenario_C.csv" &   
done


echo "Total Simulations: ${IT}"