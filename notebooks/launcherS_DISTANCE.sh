#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Sensitivity Distance:

# Scenario A

case="P"
kp=0.9

# for d in 400 600 800 1200 1600
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNAD${d}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNAD${d}_${kp} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p DISTANCE_CONTROL ${d} \
#     -p FILE "manhattan_grid_5X5_scenario_A.xml" \
#     -p DEMAND_FILE "demand_scenario_A.csv" &"
#     IT=$((IT+1))
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNAD${d}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNAD${d}_${kp} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p DISTANCE_CONTROL ${d} \
#     -p FILE "manhattan_grid_5X5_scenario_A.xml" \
#     -p DEMAND_FILE "demand_scenario_A.csv" &   
# done

# Scenario B

# for d in 400 600 800 1200 1600
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNBD${d}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNBD${d}_${kp} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p DISTANCE_CONTROL ${d} \
#     -p FILE "manhattan_grid_5X5_scenario_B.xml" \
#     -p DEMAND_FILE "demand_scenario_B.csv" &"
#     IT=$((IT+1))
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNBD${d}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNBD${d}_${kp} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p DISTANCE_CONTROL ${d} \
#     -p FILE "manhattan_grid_5X5_scenario_B.xml" \
#     -p DEMAND_FILE "demand_scenario_B.csv" &  
# done

# Scenario C

# for d in 400 600 800 1200 1600
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNCD${d}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNCD${d}_${kp} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p DISTANCE_CONTROL ${d} \
#     -p FILE "manhattan_grid_5X5_scenario_C.xml" \
#     -p DEMAND_FILE "demand_scenario_C.csv" &"
#     IT=$((IT+1))
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNCD${d}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNCD${d}_${kp} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p DISTANCE_CONTROL ${d} \
#     -p FILE "manhattan_grid_5X5_scenario_C.xml" \
#     -p DEMAND_FILE "demand_scenario_C.csv" &  
# done

# Scenario F 

for d in 400 600 800 1200 1600
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNFD${d}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT SKP_SCNFD${d}_${kp} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p DISTANCE_CONTROL ${d} \
    -p FILE "manhattan_grid_5X5_scenario_F.xml" \
    -p DEMAND_FILE "demand_scenario_F.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNFD${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT SKP_SCNFD${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_F.xml" \
    -p DEMAND_FILE "demand_scenario_F.csv" &
done

# Extra tests F 

# distance=1600

# for k in 0.05 0.65
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNFD${distance}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNFD${distance}_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${k} \
#     -p DISTANCE_CONTROL ${distance} \
#     -p FILE "manhattan_grid_5X5_scenario_F.xml" \
#     -p DEMAND_FILE "demand_scenario_F.csv" &"
#     IT=$((IT+1))
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_SCNFD${distance}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNFD${distance}_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${k} \
#     -p DISTANCE_CONTROL ${distance} \
#     -p FILE "manhattan_grid_5X5_scenario_F.xml" \
#     -p DEMAND_FILE "demand_scenario_F.csv" &
# done

# Scenario G

# for d in 400 600 800 1200 1600
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNGD${d}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNGD${d}_${kp} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p DISTANCE_CONTROL ${d} \
#     -p FILE "manhattan_grid_5X5_scenario_G.xml" \
#     -p DEMAND_FILE "demand_scenario_G.csv" &"
#     IT=$((IT+1))
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNGD${d}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT SKP_SCNGD${d}_${kp} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p DISTANCE_CONTROL ${d} \
#     -p FILE "manhattan_grid_5X5_scenario_G.xml" \
#     -p DEMAND_FILE "demand_scenario_G.csv" &  
# done


echo "Total Simulations: ${IT}"