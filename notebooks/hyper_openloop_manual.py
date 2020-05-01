""" 
    This script runs hyper paramtetrization on the simulations. 

    The objective is to collect data 

"""

# ======================================================================================================================
# Imports
# ======================================================================================================================

import papermill as pm
from itertools import product, chain

# ======================================================================================================================
# Contants
# ======================================================================================================================

# Setup experiment
EXPERIMENT = ("sensor_zone_3_3",)
CASE = (
    0,
    10,
    20,
    30,
    50,
    70,
)
CONTROL_TYPE = ("MANUAL",)
DISTANCE_CONTROL = (50,)
TRIGGER_TIME = (9000,)
SELFISH = (0.5,)
PATH_SYMUVIA = ("/Users/andresladino/Documents/01-Code/04-Platforms/dev-symuvia/build/lib/libSymuVia.dylib",)
# PATH_SYMUVIA = ("/home/ladino/dev-symuvia/build/lib/libSymuVia.so",)
SCENARIO = ("mesh30x30/",)
ZONES = ("25zones/",)
FILE = ("symuvia_network_25zones.xml",)
DEMAND_FILE = ("extnewtripset.csv",)
REF_SPEED = ("ref_speeds_25zones.csv",)
CO_KP = (1,)
CO_TI = (360,)
CO_TWD = (300,)

# General Parameters

cases = product(
    EXPERIMENT,
    CASE,
    CONTROL_TYPE,
    DISTANCE_CONTROL,
    TRIGGER_TIME,
    SELFISH,
    PATH_SYMUVIA,
    SCENARIO,
    ZONES,
    FILE,
    DEMAND_FILE,
    REF_SPEED,
    CO_KP,
    CO_TI,
    CO_TWD,
)

keys = (
    "EXPERIMENT",
    "CASE",
    "CONTROL_TYPE",
    "DISTANCE_CONTROL",
    "TRIGGER_TIME",
    "SELFISH",
    "PATH_SYMUVIA",
    "SCENARIO",
    "ZONES",
    "FILE",
    "DEMAND_FILE",
    "REF_SPEED",
    "CO_KP",
    "CO_TI",
    "CO_TWD",
)

# ======================================================================================================================
# Runtime
# ======================================================================================================================


if __name__ == "__main__":
    import pprint
    import sys

    print("Arguments", sys.argv)

    for case in cases:
        dctCase = dict(zip(keys, case))
        pprint.pprint(dctCase)
        if len(sys.argv) > 1:
            pm.execute_notebook("01_Zone_Control.ipynb", "01_Zone_Control_man.ipynb", parameters=dctCase)
