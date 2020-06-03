#!/usr/bash


# Case Open Loop 
case="OPENL"

# Scenario A
echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_dA.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT CTR_SCNA${case} \
-p CTR_ALG ${case} \
-p CONTROL_MODE ${case} \
-p FILE "manhattan_grid_5X5_A.xml" \
-p DEMAND_FILE "demand_scenario_A.csv" &"

IT=$((IT+1))

# Scenario B
echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_dB.ipynb \
-p PATH_SYMUVIA ${PATH_SYMUVIA} \
-p EXPERIMENT CTR_SCNB${case} \
-p CTR_ALG ${case} \
-p CONTROL_MODE ${case} \
-p FILE "manhattan_grid_5X5_B.xml" \
-p DEMAND_FILE "demand_scenario_B.csv" &"

IT=$((IT+1))

# Sensitivity Kp: 

# Scenario A 

case="P"

for k in  0.01 0.05 0.1 0.15 0.2
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNAKP_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
done

# Scenario B

for k in  0.01 0.05 0.1 0.15 0.2
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}_dB.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNBKP_${k} \
    -p CTR_ALG ${case} \
    -p KP ${k} \
    -p FILE "manhattan_grid_5X5_B.xml" \
    -p DEMAND_FILE "demand_scenario_B.csv" &"
    IT=$((IT+1))
done

# Sensitivity Distance:

# Scenario A

case="P"

for k in 200 400 800 1200 1600
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_DST_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNADST_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p DISTANCE_CONTROL ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
done

# Test Sensitivity Td

# Scenario A

case="PD"

for k in 100 200 300 400 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TD_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNATD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p TD ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))   
done


# Sensitivity Beta - Cooperative 3: 

# Scenario A

case="COPNL"

for k in 0.1 0.2 0.3 0.4 0.5
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_BETA_${k}_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNABETA_${k} \
    -p CTR_ALG ${case} \
    -p BETA ${k} \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))
done

# Test 3 cooperative strategies 

# Scenario A

for case in COST1 COST2 COST3
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_5x5_cost_dA.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_SCNACOST_${case} \
    -p CTR_ALG ${case} \
    -p SELFISH 0.7 \
    -p FILE "manhattan_grid_5X5_A.xml" \
    -p DEMAND_FILE "demand_scenario_A.csv" &"
    IT=$((IT+1))  
done  

# Test Network 5x5 

# for case in CO_P CO_PI P PI OPENL
# do
#    if [ "$case" == "OPENL" ]; then 
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_55.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p CTR_ALG ${case} \
#     -p CONTROL_MODE ${case} &"
#       papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_55.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p CTR_ALG ${case} \
#     -p CONTROL_MODE ${case} &
#    else
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_55.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p CTR_ALG ${case} &"
#       papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_55.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p CTR_ALG ${case} &
#    fi
# done  

# Test Network 5x5 with optimal parameters

# for case in CO_P CO_PI P PI
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_55_opt.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_OPT_${case} \
#     -p CTR_ALG ${case} \
#     -p KP 0.2 \
#     -p TI 1200 \
#     -p CO_KP 0.2 \
#     -p CO_TI 1200 \
#     -p SELFISH 0.7 &"
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_55_opt.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_OPT_${case} \
#     -p CTR_ALG ${case} \
#     -p KP 0.2 \
#     -p TI 1200 \
#     -p CO_KP 0.2 \
#     -p CO_TI 1200 \
#     -p SELFISH 0.7 &
# done  

# Test Network 3x3

# for case in CO_P CO_PI P PI OPENL
# do
#    if [ "$case" == "OPENL" ]; then 
#    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_33.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p CTR_ALG ${case} \
#     -p CONTROL_MODE ${case} \
#     -p FILE "symuvia_network_9zones.xml" \
#     -p NRow 3 \
#     -p NCol 3 \
#     -p SCENARIO "mesh9x9/" \
#     -p ZONES "9zones/" \
#     -p REF_SPEED "ref_speeds_9zones.csv" &"
#       papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_33.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p CTR_ALG ${case} \
#     -p CONTROL_MODE ${case} \
#     -p FILE "symuvia_network_9zones.xml" \
#     -p NRow 3 \
#     -p NCol 3 \
#     -p SCENARIO "mesh9x9/" \
#     -p ZONES "9zones/" \
#     -p REF_SPEED "ref_speeds_9zones.csv" &
#    else
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_33.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p CTR_ALG ${case} \
#     -p FILE "symuvia_network_9zones.xml" \
#     -p NRow 3 \
#     -p NCol 3 \
#     -p SCENARIO "mesh9x9/" \
#     -p ZONES "9zones/" \
#     -p REF_SPEED "ref_speeds_9zones.csv" &"
#       papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_33.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p CTR_ALG ${case} \
#     -p FILE "symuvia_network_9zones.xml" \
#     -p NRow 3 \
#     -p NCol 3 \
#     -p SCENARIO "mesh9x9/" \
#     -p ZONES "9zones/" \
#     -p REF_SPEED "ref_speeds_9zones.csv" &
#    fi
# done

# case="PI"

# for k in 200 360 400 500 1000
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TI_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_TI_${k} \
#     -p CTR_ALG ${case} \
#     -p TI ${k} &"
#      papermill 01_Zone_Control.ipynb 01_Zone_Control_TI_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_TI_${k} \
#     -p CTR_ALG ${case} \
#     -p TI ${k} &  
# done

# case="PI"

# for k in 1 10 50 100 500
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TWD_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_TWD_${k} \
#     -p CTR_ALG ${case} \
#     -p KP 0.2 \
#     -p TI 1200 \
#     -p TWD ${k} &"
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_TWD_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_TWD_${k} \
#     -p CTR_ALG ${case} \
#     -p KP 0.2 \
#     -p TI 1200 \
#     -p TWD ${k} &
# done

# Test Cooperative level 

# case="COP"

# for k in 0.1 0.3 0.5 0.7 0.9
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_SLF_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_SCN1SLF_${k} \
#     -p CTR_ALG ${case} \
#     -p SELFISH ${k} &"
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_SLF_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_SCN1SLF_${k} \
#     -p CTR_ALG ${case} \
#     -p SELFISH ${k} &
# done

# # Test Cooperative level KP

# case="COP"

# for k in 0.1 0.3 0.5 0.7 0.9
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_COKP_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_SCN1COKP_${k} \
#     -p CTR_ALG ${case} \
#     -p CO_KP ${k} &"
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_COKP_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_SCN1COKP_${k} \
#     -p CTR_ALG ${case} \
#     -p CO_KP ${k} &
# done

echo "Total Simulations: ${IT}"