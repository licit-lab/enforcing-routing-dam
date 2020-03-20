""" 
    This script runs hyper paramtetrization on the simulations. 

    The objective is to collect data 

"""

# ======================================================================================================================
# Imports
# ======================================================================================================================

import papermill as pm
from itertools import product

# ======================================================================================================================
# Contants
# ======================================================================================================================

# Symuvia Path
SIM = ('/Users/andresladino/Documents/01-Code/04-Platforms/dev-symuvia/build/SymuVia/libSymuVia.dylib',)

# General Parameters
PRB = (0.0, 0.1, 0.2, 0.3, 0.5, 0.7) # Vanishing Probabilities
CTR = ("MANUAL",)  # Control type
Z = ("Cpt_5",) # Zone 
D = (50,) # Minimum distance
TRGCTR = (9000,)

cases = product(PRB, CTR, Z, D, TRGCTR, SIM)
# for case in cases:
#     print(case)gt

# ======================================================================================================================
# Runtime
# ======================================================================================================================

for case in cases:
    pvan, ctr_type, zone, dst, trtime , sim = case
    print(case)
    pm.execute_notebook(
        "01_Zone_Characterisation.ipynb",
        "01_Zone_Characterisation.ipynb",
        parameters=dict(VANISHING=pvan, CONTROL_TYPE=ctr_type, ZONE=zone, DISTANCE_CONTROL=dst, TRIGGER_TIME = trtime, PATH_SYMUVIA=sim),
    )
