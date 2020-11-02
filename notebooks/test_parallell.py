"""
    This is a script that runs all possible simulations in batches of N processses determined by the user. 
    
    A time window T is also defined for running the full batch of processess. 

    The idea is to run N processess in paralell once the full batch is finished start a new one. 

    Custom functions define the output of the 
"""

# --------------------------------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------------------------------

from src.runtime.paralell import (
    combinator,
    create_chunks,
    create_db,
    create_table,
    process_chunk,
    register_simulation,
    read_schema,
    check_case_out,
    DBNAME,
)


if __name__ == "__main__":

    # Create a list of cases
    cases = combinator()

    # Create a set of chunks
    N = 30
    chunks = create_chunks(list(cases), N)

    # Create database
    create_db()
    if ("files",) not in read_schema(DBNAME).fetchall():
        create_table()

    UNDNAME = "undone.db"
    create_db(dbname=UNDNAME)
    if ("files",) not in read_schema(UNDNAME).fetchall():
        create_table(UNDNAME)

    for chunk in chunks:
        process_chunk(chunk)
        for case in chunk:
            if not check_case_out(case):
                register_simulation(case, UNDNAME)
