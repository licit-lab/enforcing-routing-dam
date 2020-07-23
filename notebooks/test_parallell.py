"""
    This is a script that runs all possible simulations in batches of N processses determined by the user. 
    
    A time window T is also defined for running the full batch of processess. 

    The idea is to run N processess in paralell once the full batch is finished start a new one. 

    Custom functions define the output of the 
"""

# --------------------------------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------------------------------

from tqdm import tqdm
from multiprocessing import Process
import time
import papermill as pm
import subprocess
from itertools import product
from collections import namedtuple
from functools import partial
import os
import glob
import sqlite3
from sqlite3 import Error

# --------------------------------------------------------------------------------------------------
# FILE MANAGEMENT
# --------------------------------------------------------------------------------------------------

DBNAME = "file_registry.db"
SQLNAME = "file_registry.sql"


def create_connection(path):
    """ Tries connecting a predetermined file"""
    connection = None
    try:
        connection = sqlite3.connect(path)
        # print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    """ Executes a query"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        # print("Query executed successfully")
        return cursor
    except Error as e:
        print(f"The error '{e}' occurred")
        return


def create_db(pathsql: str = SQLNAME, dbname: str = DBNAME):
    connection = create_connection(dbname)  # Creates demo database
    with open(pathsql) as file:
        stmt = file.readline()
        print(f"Query: {stmt}")
        execute_query(connection, stmt)


def read_schema(dbname: str = DBNAME):
    """ reads schema of a database"""
    connection = create_connection(dbname)  # Creates connection
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = execute_query(connection, query)
    return cursor


def create_table(dbname: str = DBNAME):
    """
        Create table if not existing in the db file 
    """
    query = """ CREATE TABLE files(
	sim_id IDENTITY(1,1) PRIMARY KEY,
    grid VARCHAR(160) NOT NULL,
    gain FLOAT NOT NULL,
    scenario VARCHAR(160) NOT NULL,
    distance FLOAT NOT NULL);
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
    gain,
    scenario,
    distance)
    VALUES 
    (?, ?, ?, ?);
    """
    try:
        cursor.execute(query, case)
        connection.commit()
        print("Query executed successfully")
        return cursor
    except Error as e:
        print(f"The error '{e}' occurred")
        return


def request_case(case, dbname: str = DBNAME):
    """
        Request case information 
    """
    result = execute_query(create_connection(dbname), "SELECT * FROM files")
    data = result.fetchall()
    return [x[1:] for x in data if x[1:] == case]


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
Case = namedtuple("Case", "grid gain scenario distance")


def combinator(gain: tuple = GAINS, distance: tuple = DISTANCE, scenario: tuple = SCENARIO, grid: tuple = GRID):
    """ 
        Produce all combinations
    """
    cases = product(grid, gain, scenario, distance)
    casesnt = (Case(*case) for case in cases)
    return casesnt


def create_chunks(cases, n):
    """
        Create n chunks from a list 
    """
    x = [cases[i : i + n] for i in range(0, len(cases), n)]
    return x


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
    """
        Launch a papermill for a specific case
    """
    simparameters = retrieve_sim_parameters(case)
    # pm.execute_notebook(
    #     os.path.join(os.getcwd(), simparameters["INPUT_NOTEBOOK"]),
    #     os.path.join(os.getcwd(), simparameters["OUTPUT_NOTEBOOK"]),
    #     parameters=simparameters,
    # )
    print(simparameters)
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
    for p, b in zip(proc, tqdm(range(N))):
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
            # 2. Append functions
            fns.append(partial(papermill_task, case))

    runInParallel(*fns)


if __name__ == "__main__":

    # TODO: Create a list of cases
    cases = combinator()

    # TODO: Create a set of chunks
    N = 30
    chunks = create_chunks(list(cases), N)

    # TODO: Create database
    create_db()
    if ("files",) not in read_schema(DBNAME).fetchall():
        create_table()

    process_chunk(chunks[0])

    # for chunk in chunks:
    #     process_chunk(chunk)

    #   p1 = Process(target=func1)
    #   p1.start()
    #   p2 = Process(target=func2)
    #   p2.start()
    #   p1.join()
    #   p2.join()
