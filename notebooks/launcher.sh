#!/usr/bash

PATH_SYMUVIA="/home/ladino/dev-symuvia/build/lib/libSymuVia.so"

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

for case in CO_P CO_PI P PI
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_55_opt.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_OPT_${case} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p TI 1200 \
    -p CO_KP 0.2 \
    -p CO_TI 1200 \
    -p SELFISH 0.7 &"
    papermill 01_Zone_Control.ipynb 01_Zone_Control_${case}_55_opt.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_OPT_${case} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p TI 1200 \
    -p CO_KP 0.2 \
    -p CO_TI 1200 \
    -p SELFISH 0.7 &
done  



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

# Test P for P control 

# case="P"

# for k in 0.01 0.05 0.1 0.2 0.5
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_KP_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${k} &"
#     papermill 01_Zone_Control.ipynb 01_Zone_Control_KP_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_KP_${k} \
#     -p CTR_ALG ${case} \
#     -p KP ${k} &
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

case="PI"

for k in 1 10 50 100 500
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_TWD_${k}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_TWD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p TI 1200 \
    -p TWD ${k} &"
    papermill 01_Zone_Control.ipynb 01_Zone_Control_TWD_${k}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_TWD_${k} \
    -p CTR_ALG ${case} \
    -p KP 0.2 \
    -p TI 1200 \
    -p TWD ${k} &
done

# Test Cooperative level 

# case="CO_P"

# for k in 0.1 0.3 0.5 0.7 0.9
# do
#     echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_SLF_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_SLF_${k} \
#     -p CTR_ALG ${case} \
#     -p SELFISH ${k} &"
#      papermill 01_Zone_Control.ipynb 01_Zone_Control_SLF_${k}.ipynb \
#     -p PATH_SYMUVIA ${PATH_SYMUVIA} \
#     -p EXPERIMENT CTR_SLF_${k} \
#     -p CTR_ALG ${case} \
#     -p SELFISH ${k} &   
# done

# Test Cooperative level KP

case="CO_P"

for k in 0.1 0.3 0.5 0.7 0.9
do
    echo "papermill 01_Zone_Control.ipynb 01_Zone_Control_COKP_${k}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_COKP_${k} \
    -p CTR_ALG ${case} \
    -p CO_KP ${k} &"
    papermill 01_Zone_Control.ipynb 01_Zone_Control_COKP_${k}.ipynb \
    -p PATH_SYMUVIA ${PATH_SYMUVIA} \
    -p EXPERIMENT CTR_COKP_${k} \
    -p CTR_ALG ${case} \
    -p CO_KP ${k} &
done