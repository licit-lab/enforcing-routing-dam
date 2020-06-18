#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Test Sensitivity Td

# Scenario A 

case="PD"
kp=0.65
distance=800

for k in 250 350
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

kp=0.65
distance=600

for k in 250 350
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

# kp=0.7
# distance=1200

# for k in 100 200 300 400 500
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNCK${kp}D${distance}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT STD_SCNCK${kp}D${distance}_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p TD ${k} \
#     -p DISTANCE_CONTROL ${distance} \
#     -p FILE "manhattan_grid_5X5_scenario_C.xml" \
#     -p DEMAND_FILE "demand_scenario_C.csv" &"
#     IT=$((IT+1))
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNCK${kp}D${distance}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT STD_SCNCK${kp}D${distance}_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${kp} \
#     -p TD ${k} \
#     -p DISTANCE_CONTROL ${distance} \
#     -p FILE "manhattan_grid_5X5_scenario_C.xml" \
#     -p DEMAND_FILE "demand_scenario_C.csv" &
# done

# Scenario F

kp=0.7
distance=1200

for k in 100 200 250 300 350 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNFK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNFK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_F.xml" \
    -p DEMAND_FILE "demand_scenario_F.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNFK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNFK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_F.xml" \
    -p DEMAND_FILE "demand_scenario_F.csv" &
done

# Scenario G

kp=0.7
distance=1200

for k in 250 350
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNGK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNGK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_G.xml" \
    -p DEMAND_FILE "demand_scenario_G.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_SCNGK${kp}D${distance}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT STD_SCNGK${kp}D${distance}_${k} \
    -p CTR_ALG ${case} \
    -p KP ${kp} \
    -p TD ${k} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE "manhattan_grid_5X5_scenario_G.xml" \
    -p DEMAND_FILE "demand_scenario_G.csv" &
done


# Reference cases 3 P: 0.6 /1200
case="P"

# Scenario A
# kp=0.65
# distance=800

# papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNAD${distance}.ipynb \
# -p PATH_SYMUVIA ${PATH_SYMUVIA} \
# -p EXPERIMENT SKP_SCNAD${distance}_${kp} \
# -p CTR_ALG ${case} \
# -p KP ${kp} \
# -p DISTANCE_CONTROL ${distance} \
# -p FILE "manhattan_grid_5X5_scenario_A.xml" \
# -p DEMAND_FILE "demand_scenario_A.csv" &
# IT=$((IT+1))

# Scenario B
# kp=0.65
# distance=600

# papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNBD${distance}.ipynb \
# -p PATH_SYMUVIA ${PATH_SYMUVIA} \
# -p EXPERIMENT SKP_SCNBD${distance}_${kp} \
# -p CTR_ALG ${case} \
# -p KP ${kp} \
# -p DISTANCE_CONTROL ${distance} \
# -p FILE "manhattan_grid_5X5_scenario_B.xml" \
# -p DEMAND_FILE "demand_scenario_B.csv" &
# IT=$((IT+1))       

# Scenario C
# kp=0.7
# distance=1200

# papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNCD${distance}.ipynb \
# -p PATH_SYMUVIA ${PATH_SYMUVIA} \
# -p EXPERIMENT SKP_SCNCD${distance}_${kp} \
# -p CTR_ALG ${case} \
# -p KP ${kp} \
# -p DISTANCE_CONTROL ${distance} \
# -p FILE "manhattan_grid_5X5_scenario_C.xml" \
# -p DEMAND_FILE "demand_scenario_C.csv" &
# IT=$((IT+1))

# Scenario F 
kp=0.7
distance=1200

papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNFD${distance}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT SKP_SCNFD${distance}_${kp} \
-p CTR_ALG ${case} \
-p KP ${kp} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_F.xml" \
-p DEMAND_FILE "demand_scenario_F.csv" &
IT=$((IT+1))

# Scenario G
# kp=0.7
# distance=1200

# papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${kp}_SCNGD${distance}.ipynb \
# -p PATH_SYMUVIA ${PATH_SYMUVIA} \
# -p EXPERIMENT SKP_SCNGD${distance}_${kp} \
# -p CTR_ALG ${case} \
# -p KP ${kp} \
# -p DISTANCE_CONTROL ${distance} \
# -p FILE "manhattan_grid_5X5_scenario_G.xml" \
# -p DEMAND_FILE "demand_scenario_G.csv" &
# IT=$((IT+1))




echo "Total Simulations: ${IT}"