"""
    Module of functions to extract data from XML files 
"""

from lxml import etree
import pandas as pd


def get_fields(sensor: etree._Element) -> dict:
    """
        Returns a dictionary with all the attributes for specific sensor element
    """
    return {key: sensor.get(key) for key in sensor.keys()}


def retreiveMFDData(XMLfilename):
    """ 
        Returns a dataframe with all sensor data
    """
    tree = etree.parse(XMLfilename)
    root = tree.getroot()

    # Read data
    periods = root.xpath("SIMULATION/GESTION_CAPTEUR/CAPTEURS_MFD")[0].getchildren()

    # Scan periods
    periods_df = []
    for p in periods:
        sensors = p.xpath("CAPTEURS/CAPTEUR")
        data = [get_fields(sensor) for sensor in sensors]
        df = pd.DataFrame(data)
        df["debut"] = p.get("debut")
        df["fin"] = p.get("fin")
        periods_df.append(df)

    MFDData = pd.concat(periods_df)

    # Parsing types
    dctype = {
        "concentration": float,
        "debit": float,
        "debit_sortie": float,
        "debit_sortie_int": float,
        "debit_sortie_trans": float,
        "distance_totale_parcourue": float,
        "temps_total_passe": float,
        "vitesse_spatiale": float,
        "debut": float,
        "fin": float,
    }

    MFDData = MFDData.astype(dctype)

    return MFDData


def retrieveVehData(XMLfilename):
    """ 
        Returns a dataframe with all vehicle data
    """

    tree = etree.parse(XMLfilename)
    root = tree.getroot()

    # Read data
    vehs = root.xpath("SIMULATION/VEHS")[0].getchildren()

    veh_data = []
    for veh in vehs:
        veh_data.append(get_fields(veh))

    # Pandas format
    VehData = pd.DataFrame(veh_data)

    # Parsing types
    dctype = {
        "agressif": str,
        "dstParcourue": float,
        "entree": str,
        "id": int,
        "instC": float,
        "instE": float,
        "instS": float,
        "itineraire": str,
        "kx": float,
        "lib": str,
        "sortie": str,
        "type": str,
        "vx": float,
        "w": float,
    }

    VehData = VehData.astype(dctype)

    return VehData


def retriveReroutingData(CSVfilename):
    """ 
        Returns a data frame with Rerouted data 
    """
    if CSVfilename.endswith("defaultOut_ctrlzonedata_.csv"):
        return pd.read_csv(CSVfilename, sep=";")
    return


def retriveControlData(CSVfilename):
    """ 
        Returns a data frame with Control data 
    """
    if CSVfilename.endswith("defaultOut_ctrlzonedata_probabilities.csv"):
        return pd.read_csv(CSVfilename, sep=";")
    return
