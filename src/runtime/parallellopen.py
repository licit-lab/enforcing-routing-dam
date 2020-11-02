"""
    Functions and scripts for running paralell tasks in non control files
"""
# --------------------------------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------------------------------

from itertools import product
from sqlite3 import Error
from collections import namedtuple
import os
from functools import partial
from multiprocessing import Process
import papermill as pm
from tqdm import tqdm

from src.runtime.paralell import (
    find_file,
    find_demand,
    find_refspeeds,
    request_case,
    retrive_folder_name,
    create_connection,
    execute_query,
    SCENARIO,
    GRID,
    PATH_TO_GRID,
    NCOLSGRID,
    PATH_SYMUVIA,
    DEFAULT_NOTEBOOK,
    DBNAME,
    VERSION,
    TIMEAGG,
)

# --------------------------------------------------------------------------------------------------
# FILE MANAGEMENT
# --------------------------------------------------------------------------------------------------

DBNAME = "file_registry_open.db"
SQLNAME = "file_registry_open.sql"
OUTPUT_FOLDER = os.path.join(os.getcwd(), "..", "data", "results", "mesh30x30", "")


def create_table(dbname: str = DBNAME):
    """
        Create table if not existing in the db file 
    """
    query = """ CREATE TABLE files(
	sim_id IDENTITY(1,1) PRIMARY KEY,
    grid VARCHAR(160) NOT NULL,
    scenario VARCHAR(160) NOT NULL);
    """
    connection = create_connection(dbname)
    execute_query(connection, query)


def register_simulation(case, dbname: str = DBNAME):
    """  
        Register simulation case 
    """
    connection = create_connection(dbname)
    cursor = connection.cursor()
    query = f"""
    INSERT INTO files (
    grid,
    scenario)
    VALUES 
    (?, ?);
    """
    try:
        cursor.execute(query, case)
        connection.commit()
        print("Query executed successfully")
        return cursor
    except Error as e:
        print(f"The error '{e}' occurred")
        return


# --------------------------------------------------------------------------------------------------
# FUNCTIONS
# --------------------------------------------------------------------------------------------------
CONTROL = "OPENL"
CONTROL_MODE = "MANUAL"
Case = namedtuple("Case", "grid scenario")


def combinator(scenario: tuple = SCENARIO, grid: tuple = GRID):
    """ 
        Produce all combinations
    """
    cases = product(grid, scenario)
    casesnt = (Case(*case) for case in cases)
    return casesnt


def retrieve_sim_parameters(
    case,
    input_notebook: str = DEFAULT_NOTEBOOK,
    path_symuvia: str = PATH_SYMUVIA,
    control: str = CONTROL,
    control_mode: str = CONTROL_MODE,
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
        "CONTROL_MODE": control_mode,
        "ZONES": path4grid[case.grid],
        "NRow": ncolsgrid[case.grid],
        "NCol": ncolsgrid[case.grid],
        "FILE": find_file(case)[1],
        "DEMAND_FILE": find_demand(case)[1],
        "REF_SPEED": find_refspeeds(case)[1],
    }


def retrive_folder_name(case, version: str = VERSION, timeagg: str = TIMEAGG, control: str = CONTROL):
    """ 
        Creates the scenario name for a specific case
    """
    if case:
        grid, scenario = case
        default_pre = "manhattan"
        version = version
        timeagg = timeagg
        control = control
        post = "X_X_X_X"
        name = (default_pre, scenario, version, "REF", timeagg, grid)
        return "_".join(name)
    return


def check_case_out(case, results_folder=OUTPUT_FOLDER):
    """
        Checks the existence of an output for a simulation
    """
    path4grid = PATH_TO_GRID
    fname = retrive_folder_name(case)
    path = results_folder + path4grid[case[0]] + fname
    return os.path.isdir(path) and os.path.exists(path)


def papermill_task(case):
    """
        Launch a papermill for a specific case
    """
    simparameters = retrieve_sim_parameters(case)
    pm.execute_notebook(
        os.path.join(os.getcwd(), simparameters["INPUT_NOTEBOOK"]),
        os.path.join(os.getcwd(), simparameters["OUTPUT_NOTEBOOK"]),
        parameters=simparameters,
    )
    # print(simparameters)
    return


def runInParallel(*fns):
    """
        Handle processs in paralell
    """
    proc = []
    N = -1
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
        N += 1
    for p, _ in zip(proc, tqdm(range(N))):
        p.join()


def process_chunk(chunk, dbname: str = DBNAME):
    """ 
        Processs a single chunk
    """
    fns = []
    for case in chunk:
        if case not in request_case(case, dbname):
            # 1. Register simulation (inside paralell)
            register_simulation(case, DBNAME)
            print(case)
            # 2. Append functions
            fns.append(partial(papermill_task, case))

    runInParallel(*fns)
