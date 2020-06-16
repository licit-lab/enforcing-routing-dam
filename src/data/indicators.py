"""
    Functions to compute indicators from retrieved data 
"""

import pandas as pd
import numpy as np


def pivotTTT(XMLDataFrame):
    """ 
        Pivot original DF to have TTT data in columns per sensor along time 
    """
    return XMLDataFrame.pivot(index="fin", columns="id", values="temps_total_passe")


def pivotTTD(XMLDataFrame):
    """ 
        Pivot original DF to have TTT data in columns per sensor along time 
    """
    return XMLDataFrame.pivot(index="fin", columns="id", values="distance_totale_parcourue")


def computeTTT(XMLDataFrame):
    """ 
        Find Time Exit - Time Entry
    """
    exitvalid = XMLDataFrame["instS"].ne(-1)
    return XMLDataFrame[exitvalid]["instS"] - XMLDataFrame[exitvalid]["instC"]


def compute_SPD(XMLDataFrame):
    """
        Compute speeds for all sensors 
    """
    TTD = pivotTTD(XMLDataFrame)
    TTT = pivotTTT(XMLDataFrame)

    SPD = TTD.divide(TTT)
    SPD = SPD.fillna(10)  # Free flow values
    return SPD


def TTT_var(XMLDataFrame, XMLDataFrameRef):
    """ 
        Compute TTT Variation w.r.t scenario of reference
    """

    TTT = pivotTTT(XMLDataFrame)
    TTTNC = pivotTTT(XMLDataFrameRef)
    TTT_var = (TTT.sum() - TTTNC.sum()).divide(TTTNC.sum()) * 100

    return TTT_var


def Mean_speed(XMLDataFrame):
    """ 
        Compute TTT Variation w.r.t scenario of reference
    """
    return compute_SPD(XMLDataFrame).mean()


def MS_var(XMLDataFrame, XMLDataFrameRef):
    """ 
        Compute TTT Variation w.r.t scenario of reference
    """

    SPD = compute_SPD(XMLDataFrame)
    SPDNC = compute_SPD(XMLDataFrameRef)

    return (SPD - SPDNC).divide(SPDNC).mean() * 100


def prc_rerouted(XMLDataFrame, XMLDataFrameRef):
    """ 
        Compute the % of rerouted vehicles
    """
    diffPaths = pd.concat([XMLDataFrame["itineraire"], XMLDataFrameRef["itineraire"]]).drop_duplicates(keep=False)
    nChangedPaths = diffPaths.count()
    nGeneratedVeh = XMLDataFrameRef["itineraire"].count()
    return nChangedPaths / nGeneratedVeh * 100


def mean_routing(CSVDataFrame):
    """
        Mean routing 
    """
    vehswithpath = CSVDataFrame.dropna(subset=["path"])
    countpaths = vehswithpath.groupby("veh")["time"].count()
    return countpaths.mean(), countpaths.std(), countpaths.var()


def Dup(XMLDataFrame, XMLDataFrameRef):
    """
        Mean of increase of individual travel times 
    """
    Dup = (XMLDataFrame["dstParcourue"] - XMLDataFrameRef["dstParcourue"]).divide(XMLDataFrameRef["dstParcourue"]) * 100
    Dupp = Dup[Dup > 2]
    Dup5 = np.percentile(Dup, 95)
    Dup10 = np.percentile(Dup, 90)
    return (Dup.mean(), Dupp.mean(), Dup5, Dup10)


def TWinLoose(XMLDataFrame, XMLDataFrameRef):
    """ 
        Mean % of Time Gained 
    """
    TTT = computeTTT(XMLDataFrame)
    TTTNC = computeTTT(XMLDataFrameRef)
    TSN = TTT - TTTNC
    Twin = TSN[TSN > 0]
    Tloose = -TSN[TSN < 0]
    Tloose10 = np.percentile(Tloose, 90)
    Tloose5 = np.percentile(Tloose, 95)
    PrcTSN = (TTT - TTTNC).divide(TTTNC) * 100
    PrcTwin = PrcTSN[PrcTSN > 0]
    PrcTloose = -PrcTSN[PrcTSN > 0]

    return Twin.mean(), Tloose.mean(), Tloose10, Tloose5, PrcTwin.mean(), PrcTloose.mean()
