"""
    This is a script that runs all possible simulations in batches of N processses determined by the user. 
    
    A time window T is also defined for running the full batch of processess. 

    The idea is to run N processess in paralell once the full batch is finished start a new one. 

    Custom functions define the output of the 
"""

# --------------------------------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------------------------------

from networkx.readwrite.edgelist import parse_edgelist
from tqdm import tqdm
from multiprocessing import Process
import time
import papermill as pm
import subprocess
from itertools import product
from collections import namedtuple
import os
import glob

# --------------------------------------------------------------------------------------------------
# FUNCTIONS
# --------------------------------------------------------------------------------------------------

GAINS = (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5)
DISTANCE = (200, 400, 600, 800, 1200, 1600)
SCENARIO = ("A", "B", "C", "F", "G")
SCENARIO = ("A", "B", "C", "F", "G")
GRID = ("3X3", "5X5", "7X7", "11X11")
TIMEAGG = "3"
VERSION = "V2"
CONTROL = "PN"
DEFAULT_NOTEBOOK = "01_Zone_Control.ipynb"
PATH_SYMUVIA = "/home/ladino/dev-symuvia/build/lib/libSymuVia.so"
DEFAULT_DATA_PATH = "data/scenarios/mesh30x30/"
PATH_TO_GRID = {"3X3": "9zones/", "5X5": "25zones/", "7X7": "49zones/", "11X11": "121zones/"}
NCOLSGRID = {"3X3": 3, "5X5": 5, "7X7": 7, "11X11": 11}


def combinator(gain: tuple = GAINS, distance: tuple = DISTANCE, scenario: tuple = SCENARIO, grid: tuple = GRID):
    """ 
        Produce all combinations
    """
    cases = product(grid, gain, scenario, distance)
    Case = namedtuple("Case", "grid gain scenario distance")
    casesnt = (Case(*case) for case in cases)
    return casesnt


def retrive_folder_name(case, version: str = VERSION, timeagg: str = TIMEAGG, control: str = CONTROL):
    """ 
        Creates the scenario name for a specific case
    """
    if case:
        grid, gain, scenario, distance = case
        default_pre = "manhattan"
        version = version
        timeagg = timeagg
        control = control
        post = "X_X_X"
        name = (default_pre, scenario, version, timeagg, str(distance), grid, control, str(gain), post)
        return "_".join(name)
    return


def find_file(case, path: str = DEFAULT_DATA_PATH):
    """ 
        Return full path name of a case
    """
    path2search = os.path.join(os.getcwd(), "..", path)
    path4grid = PATH_TO_GRID
    filechk = lambda files, case: [x for x in files if case + ".xml" in x]
    for p in os.walk(path2search):
        last = p[0].split("/")[-1]
        if last == path4grid[case.grid][:-1]:
            files = glob.glob(p[0] + "/*.xml")
            file = filechk(files, case.scenario)[0]
            return file, file.split("/")[-1]
    return


def find_demand(case, path: str = DEFAULT_DATA_PATH):
    """ 
        Return full path name of a demand for scenario
    """
    path2search = os.path.join(os.getcwd(), "..", path)
    x = glob.glob(path2search + f"/*{case.scenario}.csv")
    return x[0], x[0].split("/")[-1]


def find_refspeeds(case, path: str = DEFAULT_DATA_PATH):
    """
        Find reference's speed file
    """
    path2search = os.path.join(os.getcwd(), "..", path)
    path4grid = PATH_TO_GRID
    for p in os.walk(path2search):
        last = p[0].split("/")[-1]
        if last == path4grid[case.grid][:-1]:
            ptrn = p[0] + f"/*{case.grid}.csv"
            file = glob.glob(ptrn)
            return file[0], file[0].split("/")[-1]
    return


def retrieve_sim_parameters(
    case, input_notebook: str = DEFAULT_NOTEBOOK, path_symuvia: str = PATH_SYMUVIA, control: str = CONTROL
):
    """ 
        Returns a dictionary containing the whole set of parameters for a single run
    """
    preinput, postinput = input_notebook.split(".")
    path4grid = PATH_TO_GRID
    ncolsgrid = NCOLSGRID
    return {
        "INPUT_NOTEBOOK": input_notebook,
        "OUTPUT_NOTEBOOK": preinput + "_" + retrive_folder_name(case) + "." + postinput,
        "PATH_SYMUVIA": path_symuvia,
        "EXPERIMENT": retrive_folder_name(case, control=control),
        "CTR_ALG": control,
        "KP": case.gain,
        "DISTANCE_CONTROL": case.distance,
        "ZONES": path4grid[case.grid],
        "NRow": ncolsgrid[case.grid],
        "NCol": ncolsgrid[case.grid],
        "FILE": find_file(case)[1],
        "DEMAND_FILE": find_demand(case)[1],
        "REF_SPEED": find_refspeeds(case)[1],
    }


def papermill_task(case):
    simparameters = retrieve_sim_parameters(case)
    # pm.execute_notebook(
    print(
        os.path.join(os.getcwd(), simparameters["INPUT_NOTEBOOK"]),
        os.path.join(os.getcwd(), simparameters["OUTPUT_NOTEBOOK"]),
        parameters=simparameters,
    )
    return


def func1():
    print("func1: starting")
    time.sleep(1)
    print("func1: finishing")


def func2():
    print("func2: starting")
    time.sleep(2)
    print("func2: finishing")


def func3():
    subprocess.run(["echo", "2"])


def runInParallel(*fns):
    """
        Handle processs in paralell
    """
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


if __name__ == "__main__":
    #   p1 = Process(target=func1)
    #   p1.start()
    #   p2 = Process(target=func2)
    #   p2.start()
    #   p1.join()
    #   p2.join()
    runInParallel(func3, func3)

    for i in tqdm(range(int(1560))):
        time.sleep(0.001)
