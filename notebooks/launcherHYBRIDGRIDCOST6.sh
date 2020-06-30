#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
IT=0

OLDIFS=$IFS; IFS=',';

# Scenario B
td=0.0

case="COSTN6"
alpha=0.1

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done

alpha=0.2

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done

alpha=0.3

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done

alpha=0.4

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done

alpha=0.5

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done

alpha=0.6

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done

alpha=0.7

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done

alpha=0.8

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done

alpha=0.9

for i in manhattan_grid_3X3_scenario_B.xml,9zones/,ref_speeds_3X3.csv,3X3,3,0.2,400 \
manhattan_grid_7X7_scenario_B.xml,49zones/,ref_speeds_7X7.csv,7X7,7,0.6,1200 \
manhattan_grid_11X11_scenario_B.xml,121zones/,ref_speeds_11X11.csv,11X11,11,0.6,1200
do
    set -- $i
    echo "Running: $1 and $2 and $3 and $4 and $5 and $6 and $7"
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_ALPHA_${alpha}_SCNBD$7K$6_$4.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT manhattan_B_V2_3_$7_$4_${case}_$6_${td}_${alpha}_X_X_X_FIX \
    -p CTR_ALG ${case} \
    -p SELFISH ${alpha} \
    -p KP $6 \
    -p CO_KP $6 \
    -p TD ${td} \
    -p CO_TD ${td} \
    -p DISTANCE_CONTROL $7 \
    -p FILE $1 \
    -p ZONES $2 \
    -p REF_SPEED $3 \
    -p NRow $5 \
    -p NCol $5 \
    -p DEMAND_FILE "demand_scenario_B.csv" &     
done