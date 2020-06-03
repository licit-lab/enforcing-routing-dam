""" 
    Functions to operate over data 
    
"""


# Extract demand
def extract_veh_data(demand, time):
    """
        This function extracts vehicle deta from the demand
        
        demand should predefined
    """
    # Filter
    creation_query = f"{time} < creation<={time+1}"
    current_demand = demand.query(creation_query)

    # Generator
    for _, veh in current_demand.iterrows():
        yield (veh["typeofvehicle"], veh["origin"], veh["destination"], 1, veh["creation"], veh["path"])
