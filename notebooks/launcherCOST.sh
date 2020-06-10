#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Cooperative strategies 

# Scenario A

for case in COST2 COST3 COST5 COST6
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_SCNAD800K05TD200.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT COST_SCNAD800K05TD200_${case} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP 0.5 \
    -p CO_KP 0.5 \
    -p TD 200 \
    -p CO_TD 200 \
    -p DISTANCE_CONTROL 800 \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))    
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_SCNAD800K05TD200.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT COST_SCNAD800K05TD200_${case} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP 0.5 \
    -p CO_KP 0.5 \
    -p TD 200 \
    -p CO_TD 200 \
    -p DISTANCE_CONTROL 800 \
    -p FILE "manhattan_grid_5X5_scenario_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &    
done  

# Scenario B

for case in COST2 COST3 COST5 COST6
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_SCNBD800K05TD200.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT COST_SCNBD800K05TD200_${case} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP 0.5 \
    -p CO_KP 0.5 \
    -p TD 200 \
    -p CO_TD 200 \
    -p DISTANCE_CONTROL 800 \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))    
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_SCNBD800K05TD200.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT COST_SCNBD800K05TD200_${case} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.5 \
    -p KP 0.5 \
    -p CO_KP 0.5 \
    -p TD 200 \
    -p CO_TD 200 \
    -p DISTANCE_CONTROL 800 \
    -p FILE "manhattan_grid_5X5_scenario_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done  

echo "Total Simulations: ${IT}"