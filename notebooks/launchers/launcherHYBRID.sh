#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Cooperative strategies 

# Scenario A
kp=0.65
td=0.0
distance=800

case="COSTH4"
alpha=0.2

echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &"
IT=$((IT+1))
papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &

case="COSTN4"
alpha=0.2

echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &"
IT=$((IT+1))
papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &

case="COSTH6"
alpha=0.2

echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &"
IT=$((IT+1))
papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &

case="COSTN6"
alpha=0.2

echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &"
IT=$((IT+1))
papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_A_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &

# Scenario B

kp=0.65
td=0.0
distance=600

case="COSTH4"
alpha=0.2

echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &"
IT=$((IT+1))
papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &

case="COSTN4"
alpha=0.2

echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &"
IT=$((IT+1))
papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &

case="COSTH6"
alpha=0.2

echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &"
IT=$((IT+1))
papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &

case="COSTN6"
alpha=0.2

echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &"
IT=$((IT+1))
papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD${distance}K${kp}.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT manhattan_B_V2_3_${distance}_5X5_${case}_${kp}_${td}_${alpha}_X_X_X \
-p CTR_ALG ${case} \
-p SELFISH ${alpha} \
-p KP ${kp} \
-p CO_KP ${kp} \
-p TD ${td} \
-p CO_TD ${td} \
-p DISTANCE_CONTROL ${distance} \
-p FILE "manhattan_grid_5X5_scenario_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" \
-p REF_SPEED "ref_speeds_25zones.csv" &