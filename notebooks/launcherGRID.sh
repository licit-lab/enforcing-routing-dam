#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

# Scenario A
kp=0.65
td=0.0
distance=800

case="COSTN4"
alpha=0.5

for i in manhattan_grid_3X3_scenario_A.xml,9zones/,ref_speeds_3X3.csv,3X3,3 \
manhattan_grid_7X7_scenario_A.xml,49zones/,ref_speeds_7X7.csv,7X7,7 \
manhattan_grid_11X11_scenario_A,121zones/,ref_speeds_11X11.csv,11X11,11
do IFS=","
    set -- $i
    echo "Running: $1 and $2 and $3"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_A.csv" &     
done

case="COSTN6"
alpha=0.2

for i in manhattan_grid_3X3_scenario_A.xml,9zones/,ref_speeds_3X3.csv,3X3,3 \
manhattan_grid_7X7_scenario_A.xml,49zones/,ref_speeds_7X7.csv,7X7,7 \
manhattan_grid_11X11_scenario_A,121zones/,ref_speeds_11X11.csv,11X11,11
do IFS=","
    set -- $i
    echo "Running: $1 and $2 and $3"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_A.csv" &  
done


case="COSTN6"
alpha=0.5

for i in manhattan_grid_3X3_scenario_A.xml,9zones/,ref_speeds_3X3.csv,3X3,3 \
manhattan_grid_7X7_scenario_A.xml,49zones/,ref_speeds_7X7.csv,7X7,7 \
manhattan_grid_11X11_scenario_A,121zones/,ref_speeds_11X11.csv,11X11,11
do IFS=","
    set -- $i
    echo "Running: $1 and $2 and $3"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_A_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_A.csv" &      
done


# Scenario B
kp=0.65
td=0.0
distance=600

case="COSTN4"
alpha=0.2

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7 \
manhattan_grid_11X11_scenario_B,121zones/,ref_speeds_11X11.csv,11X11,11
do IFS=","
    set -- $i
    echo "Running: $1 and $2 and $3"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &         
done


case="COSTN6"
alpha=0.4

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7 \
manhattan_grid_11X11_scenario_B,121zones/,ref_speeds_11X11.csv,11X11,11
do IFS=","
    set -- $i
    echo "Running: $1 and $2 and $3"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNAD${distance}K${kp}_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_${distance}_$4_${case}_${kp}_${td}_${alpha}_X_X_X \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP ${kp} \
    -p CO_KP ${kp} \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL ${distance} \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &         
done

echo "Total Simulations: ${IT}"