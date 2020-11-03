"""
    Functions to compute indicators from retrieved data 
"""

import pandas as pd
import numpy as np


def pivotTTT(XMLDataFrame):
    """ 
        Pivot original DF to have TTT data in columns per sensor along time 
    """
    return XMLDataFrame.pivot(
        index="fin", columns="id", values="temps_total_passe"
    )


def pivotTTD(XMLDataFrame):
    """ 
        Pivot original DF to have TTT data in columns per sensor along time 
    """
    return XMLDataFrame.pivot(
        index="fin", columns="id", values="distance_totale_parcourue"
    )


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
    TTD = pivotTTD(XMLDataFrame)
    TTT = pivotTTT(XMLDataFrame)

    return TTD.sum() / TTT.sum()


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
    # diffPaths = pd.concat(
    #     [XMLDataFrame["itineraire"], XMLDataFrameRef["itineraire"]]
    # ).drop_duplicates(keep=False)
    # nChangedPaths = diffPaths.count()
    # nGeneratedVeh = XMLDataFrameRef["itineraire"].count()
    nChangedPaths = len(
        [
            i
            for i, j in zip(
                XMLDataFrame["itineraire"], XMLDataFrameRef["itineraire"]
            )
            if i != j
        ]
    )
    nGeneratedVeh = len(XMLDataFrame["id"])
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
    Dup = (
        XMLDataFrame["dstParcourue"] - XMLDataFrameRef["dstParcourue"]
    ).divide(XMLDataFrameRef["dstParcourue"]) * 100
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
    PrcTloose = -PrcTSN[PrcTSN < 0]

    return (
        Twin.mean(),
        Tloose.mean(),
        Tloose10,
        Tloose5,
        PrcTwin.mean(),
        PrcTloose.mean(),
    )


def TwinLooseDup(XMLDataFrame, XMLDataFrameRef):

    idvehs = list(XMLDataFrame.id)

    ttds = []
    ttts = []

    for i, r in XMLDataFrame.iterrows():
        if r["instS"] != "-1.00":
            ttds.append(r["dstParcourue"])
            ttts.append(r["instS"] - r["instC"])
        else:
            ttds.append(-1.0)
            ttts.append(-1.0)

    ttts_ref = []
    ttds_ref = []

    for i, r in XMLDataFrameRef.iterrows():
        if r["instS"] != "-1.00":
            ttds_ref.append(r["dstParcourue"])
            ttts_ref.append(r["instS"] - r["instC"])
        else:
            ttds_ref.append(-1.0)
            ttts_ref.append(-1.0)

    tds_win = []
    v_tds_win = []
    tds_loose = []
    v_tds_loose = []
    dds = []

    for v in range(len(idvehs)):

        if ttds[v] > 0 and ttts[v] > 0 and ttds_ref[v] > 0 and ttts_ref[v] > 0:
            dds.append((ttds[v] - ttds_ref[v]) / ttds_ref[v] * 100)

    for v in range(len(idvehs)):
        # if paths[v]!=paths_ref[v] and ttds[v]>0 and ttts[v]>0 and ttds_ref[v]>0 and ttts_ref[v]>0:
        if ttds[v] > 0 and ttts[v] > 0 and ttds_ref[v] > 0 and ttts_ref[v] > 0:
            dds.append((ttds[v] - ttds_ref[v]) / ttds_ref[v] * 100)

            if ttts[v] < ttts_ref[v]:
                v_tds_win.append(idvehs[v])
                tds_win.append(-(ttts[v] - ttts_ref[v]) / ttts_ref[v] * 100)

            if ttts[v] > ttts_ref[v]:
                v_tds_loose.append(idvehs[v])
                tds_loose.append((ttts[v] - ttts_ref[v]) / ttts_ref[v] * 100)

    Dup = sum(dds) / float(len(dds))

    # Dup+
    dds_supp = []
    for d in dds:
        if d > 0.02:
            dds_supp.append(d)

    Dupp = sum(dds_supp) / float(len(dds_supp))
    # print('Dup',Dupp)

    # Dup_10
    Dup_10 = round(np.percentile(dds, 90), 2)

    # Dup_5
    Dup_5 = round(np.percentile(dds, 95), 2)

    # %Twin
    PrcTwin = round(len(v_tds_win) / (len(v_tds_win) + len(v_tds_loose)), 2)

    # %Tloose
    PrcTloose = round(len(v_tds_loose) / (len(v_tds_win) + len(v_tds_loose)), 2)

    # Twin
    Twin = sum(tds_win) / float(len(tds_win))
    # print('Twin',Twin)

    # Tloose
    Tloose = sum(tds_loose) / float(len(tds_loose))
    # print('Tloose',Tloose)

    # Tloose_10
    Tloose_10 = round(np.percentile(tds_loose, 90), 2)

    # Tloose_5
    Tloose_5 = round(np.percentile(tds_loose, 95), 2)

    return (
        Dup,
        Dupp,
        Dup_10,
        Dup_5,
        PrcTwin,
        PrcTloose,
        Twin,
        Tloose,
        Tloose_10,
        Tloose_5,
    )


def networkHomogeneity(XMLDataFrame):
    """
        Variance of average speeds in zones
    """
    SPD = compute_SPD(XMLDataFrame)
    return SPD.mean().drop(["sensor_network"]).std()
