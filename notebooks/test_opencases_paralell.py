"""
    This is a script that runs all possible open loop simulations in batches of N processses determined by the user. 
    
    A time window T is also defined for running the full batch of processess. 

    The idea is to run N processess in paralell once the full batch is finished start a new one. 

    Custom functions define the output of the simulations
"""

# --------------------------------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------------------------------
from src.runtime.paralell import create_chunks, create_db, read_schema

from src.runtime.parallellopen import (
    execute_query,
    create_connection,
    create_table,
    register_simulation,
    combinator,
    check_case_out,
    process_chunk,
    Case,
    DBNAME,
)


def check_missing_cases():
    UNDNAME = "undone_open.db"
    query = "SELECT * FROM files"
    missing = execute_query(create_connection(UNDNAME), query)
    missingcases = [Case(*x[1:]) for x in missing]
    return missingcases


if __name__ == "__main__":

    # Create a list of cases
    cases = combinator()

    # Create a set of chunks
    N = 30
    chunks = create_chunks(cases, N)

    # Emergency
    UNDNAME = "undone_open.db"
    create_db(dbname=UNDNAME)
    if ("files",) not in read_schema(UNDNAME).fetchall():
        create_table(UNDNAME)

    # New registry
    NEWCASES = "file_registry_open.db"
    create_db(dbname=NEWCASES)
    if ("files",) not in read_schema(NEWCASES).fetchall():
        create_table(NEWCASES)

    # Chunks
    for i, chunk in enumerate(chunks):
        print(f"Trying chunk {i}")
        process_chunk(chunk, NEWCASES)
        for case in chunk:
            if not check_case_out(case):
                register_simulation(case, UNDNAME)
