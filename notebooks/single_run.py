""" 
    This script runs the equivalent of 01_Zone_Caracterisation. 

    Useful for debugging purposes
"""

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Effect of Vanishing Policies in traffic rerouting
#
# **Objective**
# * The objective is to perform an analysis to determine the impact of introducing vanishing policies in specific zones of a city.
#
# <img src="../images/zones.png" alt="drawing" width="400"/>
#

# %%
# Parameters
ZONE = "Cpt_5"
VANISHING = 0.4
CONTROL_TYPE = "MANUAL"
DISTANCE_CONTROL = 50


# %%
import subprocess
import symupy
import pandas as pd
import numpy as np
import os
import sys
import re
from itertools import repeat, chain
import ipywidgets as widgets
from IPython.display import display
import networkx as nx

try:
    pd.set_option("plotting.backend", "hvplot")
except:
    pass
print(f"Backend: {pd.options.plotting.backend}")

from symupy.api import Simulator, Simulation

print(f"Version of symupy: {symupy.__version__}")

packages = ["src"]

# Adding supplementary functions
for pck in packages:
    print(f"Adding folder: {pck}")
    sys.path.append(os.path.join(os.getcwd(), f"../{pck}"))


# %%
# Path information
PATH_SYMUVIA = "/Users/andresladino/Documents/01-Code/04-Platforms/dev-symuvia/build/SymuVia/libSymuVia.dylib"  # Laptop
# PATH_SYMUVIA = '/Users/ladino/Documents/01-Platforms/01-Symuvia/06-Source/01-VanishingZones/build/SymuVia/libSymuVia.dylib' # Office

PATH_SCENARIO = os.getcwd() + "/../data/scenarios/mesh9x9/net1_nodemand_9zones2.xml"  # Laptop
# PATH_SCENARIO = '/Users/ladino/Dropbox/02-PostDoc/03-Research/07-Publications/02-In_review/ISTTT2021/Partage_ISTTT24/Dev/Data/Mesh9zones/net1_nodemand_9zones2.xml' # Office

DATA_INPUT = "../data/scenarios/mesh9x9/"  # Laptop
# bannedzone_input = '/Users/ladino/Dropbox/02-PostDoc/03-Research/07-Publications/02-In_review/ISTTT2021/Partage_ISTTT24/Dev/Data/Mesh9zones/' # Office

# %% [markdown]
# #### File reading
#
# * Read zone links and construct a list of strings by containing links per zone `zone2_Cpt_*.csv`
# * Read demand file `extnewtripset.csv`

# %%
# Zone information

files = [f for f in os.listdir(DATA_INPUT) if re.search(r"\d.csv$", f)]

# Data management
df_zones = []

# Communicate to Symuvia
dct_ctrl = {}

# Reading all files
for file in files:
    key = file.split("_")[-1][0]  # Zone number
    df_zone = pd.read_csv(DATA_INPUT + file, header=None, names=["Link"])
    df_zone["Zone"] = key
    df_zones.append(df_zone)
    ls_links = " ".join(df_zone["Link"].to_list())
    dct_ctrl[key] = f"'{ls_links}'"  # This special to have "'x'" instead of 'x'

# All zone data is here
df_zones = pd.concat(df_zones)
# df_zones.head()


# %%
# Demand information
dfile = "extnewtripset.csv"
demand = pd.read_csv(DATA_INPUT + dfile, sep=";")
demand.rename({"Unnamed: 0": "vehid"}, axis=1, inplace=True)  # Rename column
# demand.head()


# %%
# Some idea of the flow
TIME_MAX = demand.creation.max()
TIME_MIN = demand.creation.min()
DELTA_TIME = TIME_MAX - TIME_MIN
interval_cut = pd.cut(demand.creation, int(DELTA_TIME / 60))
flow = demand.groupby(interval_cut).count()
flow["stamp"] = np.arange(len(flow))
# flow.plot(x='stamp',y='creation',grid = True, title = 'Aggregated Demand')


# %%
# Vehicle creation
numveh = demand.groupby(interval_cut).max()
numveh["stamp"] = np.arange(len(numveh))
# numveh.plot(x='stamp',y='creation',grid = True, title = 'Aggregated Demand')

# %% [markdown]
# #### Recreation of a demand
#
# As it can be observed the demand profile here assumed is only valid for the first 150 minutes. In order to reach equilibria we propose to sample vehicles uniformly within this interval to create the amount of vehicles for the following 100 seconds.

# %%
TIME_LIMIT = 150
constant_demand = demand.query(f"creation<={TIME_LIMIT * 60}")
id_new_veh = constant_demand.vehid.max()

# Creating new demand
extra_demand = constant_demand.copy()
# Shifting new vehicles instant
extra_demand["creation"] = extra_demand["creation"].apply(lambda x: x + TIME_LIMIT * 60)
extra_demand["vehid"] = extra_demand["vehid"].apply(lambda x: x + id_new_veh)
# Shifting vehicle instant creation
extra_demand.head()

TIME_MAX = extra_demand.creation.max()
TIME_MIN = extra_demand.creation.min()
DELTA_TIME = TIME_MAX - TIME_MIN

interal_cut = pd.cut(extra_demand.creation, bins=int(DELTA_TIME / 60))

extra_flow = extra_demand.groupby(interal_cut).count()
extra_flow["stamp"] = np.arange(len(extra_flow))
# extra_flow.plot(x='stamp',y='creation',grid = True, title = 'Extended Demand')


# %%
demand = pd.concat([constant_demand, extra_demand])

MAX_TIME = demand.creation.max()

flow = demand.groupby(pd.cut(demand.creation, int(demand.creation.max() / 60))).count()
flow["stamp"] = np.arange(len(flow))
# flow.plot(x='stamp',y='creation',grid = True, title = 'Aggregated Demand')

# %% [markdown]
# ### Launch simulation
#
# The objective of the following part is to perform a step by step simulation in multiple scenarios.
#
# #### Scenario generation
#
# This instantiate and generate the scenario for the simulation

# %%
# Simulation creation
simulator = Simulator(PATH_SYMUVIA)
scenario = Simulation(PATH_SCENARIO)

# Register simulation
simulator.register_simulation(scenario)

# Sensors
sensors = list(scenario.get_mfd_sensor_names())
sensors.pop()
# takes out Global

# %% [markdown]
# #### Supplementary functions
#
# Define all supplementary functions required for the control

# %%
from data.transformer import extract_veh_data
from algorithms.control import define_grid_graph, compute_vanishing_control

# Progress bar
max_count = 100

# progress =  widgets.IntProgress(
#     value=0,
#     min=0,
#     max=max_count,
#     step=1,
#     description='Progress:',
#     bar_style='success', # 'success', 'info', 'warning', 'danger' or ''
#     orientation='horizontal'
# ) # instantiate the bar

# Create cooperative graph
G = define_grid_graph(3, 3)
# nx.draw(G, node_color="#A0CBE2", with_labels=True) # Plot

# %% [markdown]
# #### Control policy
#
# Here we set the control policy

# %%
# Control

state_A = dict(zip(sensors, repeat(0)))

state_B = dict(zip(sensors, repeat(0)))
state_B[ZONE] = VANISHING

TRIGGER_TIME = 9000

if CONTROL_TYPE == "MANUAL":
    compute_control = lambda time, threshold, speed, graph: state_B if time > threshold else state_A
elif CONTROL_TYPE == "AUTO":
    compute_control = compute_vanishing_control
else:
    compute_control = lambda time, threshold, speed, graph: state_A


# Distance control action
dstcontrol = dict(zip(sensors, repeat(DISTANCE_CONTROL)))

# %% [markdown]
# #### Runtime simulations
#
# The following launches the runtime simulations.

# %%
# Runtime
TTT = []
TTD = []
SPD = []
CTR = []

# Simulation runtime
# display(progress) # display the bar

# Control time
control_interval = 180  # seconds


vehids = []

with simulator as s:
    #     progress.value = 0
    while s.do_next:
        s.run_step()

        # Vehicle creation on demand
        for veh_data in extract_veh_data(demand, s.time_step):
            vehid = s.create_vehicle_with_route(*veh_data)
            vehids.append(vehid)

        if not s.simulationstep % control_interval and s.simulationstep > 0:
            #             progress.value += 1
            TTD.append(dict(zip(sensors, s.get_total_travel_distance())))
            TTT.append(dict(zip(sensors, s.get_total_travel_time())))
            SPD.append(dict(zip(sensors, s.get_mfd_speed())))

            control_rate = compute_control(s.simulationstep, TRIGGER_TIME, SPD[-1], G)
            CTR.append(control_rate)
            print(control_rate)

            s.modify_control_probability_zone_mfd(control_rate)

        if s.simulationstep == 0:
            control_rate = state_A
            CTR.append(control_rate)
            s.add_control_probability_zone_mfd(control_rate, dstcontrol)


# %%
# Save files
output_dir = os.getcwd() + f"/../data/results/{ZONE}_{CONTROL_TYPE}_{int(VANISHING*100)}/"
output_dir


# %%
# get_ipython().system("mkdir -p $output_dir")
dircrt = subprocess.run(["mkdir", "-p", output_dir])


# %%
# Results saving

# DataFrames
ttd = pd.DataFrame(TTD)
ttt = pd.DataFrame(TTT)
spd = pd.DataFrame(SPD)
ctr = pd.DataFrame(CTR)

if dircrt == 0:
    ttt.to_csv(output_dir + "ttt.csv", index=False)
    ttd.to_csv(output_dir + "ttd.csv", index=False)
    spd.to_csv(output_dir + "spd.csv", index=False)
    ctr.to_csv(output_dir + "ctr.csv", index=False)
else:
    print("Something is wrong with directory creation")
    ttt.to_csv("ttt.csv", index=False)
    ttd.to_csv("ttd.csv", index=False)
    spd.to_csv("spd.csv", index=False)
    ctr.to_csv("ctr.csv", index=False)

# %% [markdown]
# Andres L.
