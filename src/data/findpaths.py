""" 
    1. Scan each folder and retrieve Sensor / Vehicle/ Probability/ Routing data
    2. Compute the following indicators:
        TTT_var	
            TTT_var	Variation du TTT total entre contrôle et sans contrôle en %
        TTT_var_i	
            Variation du TTT total (sur toute la durée de la simulation) dans la zone i entre contrôle et sans contrôle en %
        Mean_speed	
            Vitesse moyenne sur tout le réseau pour toute la simulation (calculé dans le cas contrôlé et non contrôlé)
        Mean_speed_i	
            Vitesse moyenne dans la région i pour toute la simulation (inclure le tour extérieur comme une région) (calculé dans le cas contrôlé et non contrôlé)
        MS_var	
            Variation de Mean_speed entre contrôle et sans contrôle en %
        MS_var_i	
            Variation de Mean_speed_i entre contrôle et sans contrôle en %
        %_routedveh	
            Nb de véhicules reroutés au moins un fois / Nb total de véhicule généré
        Mean_routing	
            Nb moyen de reroutage (uniquement pour les véhicules ayant été reroutés au moins une fois)
        Var_routing	
            Variance du nombre de reroutage (uniquement les véhicules ayant été reroutés au moins une fois)
        Dup	
            Moyenne de l'accroissement des distances individuelles
        Dup+	
            Moyenne de l'accroissement des distances individuelles en ne tenant compte que celle >2%
        Dup_10	
            Percentile 10% sup sur l'accroissement des distances (% d'accroissement expérimentés par seulement 10% des individus)
        Dup_5	
            Percentile 5% sup sur l'accroissement des distances (% d'accroissement expérimentés par seulement 5% des individus)
        %Twin	
            Fraction des véhicules qui obtiennent un gain de temps de parcours par le contrôle
        %Tloose	
            Fraction des véhicules qui obtiennent une perte de temps de parcours par le contrôle
        Twin	
            Moyenne des gains individus de véhicules en % (moyenne des Twin)
        Tloose	
            Moyenne des pertes individuels des véhicules en %
        Tloose_10	
            Perte de temps de parcours expérimentés par seulement 10% de la population
        Tllose_5	
            Perte de temps de parcours expérimentés par seulement 5% de la populationVariation du TTT total entre contrôle et sans contrôle en %
"""

import glob
import os
import pandas as pd
from operator import itemgetter
from indicators import (
    TTT_var,
    Mean_speed,
    MS_var,
    prc_rerouted,
    Dup,
    mean_routing,
    TWinLoose,
    networkHomogeneity,
    TwinLooseDup,
)

from dataloader import (
    retreiveMFDData,
    retrieveVehData,
    retriveControlData,
    retriveReroutingData,
)


def locate_filenames(general_path):
    """ 
        Locate XML files within a general path 
    """
    fullPathslist = []
    for path, folder, _ in os.walk(general_path):
        fullpaths = {}
        if not folder:
            xmlfile = glob.glob(path + "/*_traf.xml")
            controlfile = glob.glob(
                path + "/defaultOut_ctrlzonedata_probabilities.csv"
            )
            routingfile = glob.glob(path + "/defaultOut_ctrlzonedata_.csv")
            try:
                fullpaths["xml"] = xmlfile[0]
            except IndexError:
                fullpaths["xml"] = None
            try:
                fullpaths["ctr"] = controlfile[0]
            except IndexError:
                fullpaths["ctr"] = None
            try:
                fullpaths["rou"] = routingfile[0]
            except IndexError:
                fullpaths["rou"] = None
            fullPathslist.append(fullpaths)
    return fullPathslist


def categorize_path(xmlfilename):
    """
        Return case name from full path. 
    """
    parts = xmlfilename.split("/")
    for part in parts:
        if "manhattan" in part:
            return part


def match_cases(dfCases):
    """
        Makes a match between the Controlled scenarios and uncontrolled scenarios
    """
    dfCases["ref"] = dfCases.apply(lambda x: "REF" in x["xml"], axis=1)
    dfCases["case"] = dfCases.apply(lambda x: categorize_path(x["xml"]), axis=1)

    dfNoControl = dfCases[dfCases.ref]
    dfControl = dfCases[~dfCases.ref]

    dfNoControl["key"] = dfNoControl.apply(
        lambda x: itemgetter(*[0, 1, 4, 5])(x["case"].split("_")), axis=1
    )

    dfControl["key"] = dfControl.apply(
        lambda x: itemgetter(*[0, 1, 3, 5])(x["case"].split("_")), axis=1
    )

    # For case processing tracking purposes
    dfControl["keyfile"] = dfControl.apply(
        lambda x: itemgetter(*[0, 1, 3, 4, 5, 6, 7])(x["case"].split("_")),
        axis=1,
    )

    dfNoControl.rename(columns={"xml": "noctr"}, inplace=True)

    dfMatched = pd.merge(dfControl, dfNoControl[["noctr", "key"]], on="key")

    return dfMatched


# Moved to main

# if __name__ == "__main__":
#     gen_path = os.getcwd()
#     print(f"Analyzing: {gen_path}")
#     cases = locate_filenames(gen_path)
#     dfCases = pd.DataFrame(cases)
#     dfCases = dfCases.dropna(subset=["xml"])  # Cleaning non xml file folders

#     # This updates the dataframe with multiple columns 'key','noctr' denoting the corresponding non control scenario for each scenario
#     dfCases = match_cases(dfCases)

#     datalist = []
#     # Load all data
#     for index, row in dfCases.iterrows():

#         # Filenames for reference

#         xmlfile = row.xml
#         ctrfile = row.ctr
#         roufile = row.rou
#         ncxmlfile = row.noctr

#         print(f"{categorize_path(xmlfile)} \t- {categorize_path(ncxmlfile)}")

#         # Retrieve closed loop data
#         dfMFD = retreiveMFDData(xmlfile)
#         dfVeh = retrieveVehData(xmlfile)
#         dfRoute = retriveReroutingData(roufile)
#         dfCtr = retriveControlData(ctrfile)

#         # Retreive Open loop data
#         dfMFDNC = retreiveMFDData(ncxmlfile)
#         dfVehNC = retrieveVehData(ncxmlfile)

#         # Indicators computation
#         TTTVar = TTT_var(dfMFD, dfMFDNC)
#         MeanSpeed = Mean_speed(dfMFD)
#         MeanSpeedNC = Mean_speed(dfMFDNC)
#         MSVar = MS_var(dfMFD, dfMFDNC)
#         PrcRouted = prc_rerouted(dfVeh, dfVehNC)
#         (
#             DUp,
#             DUpp,
#             DUp5,
#             DUp10,
#             PrcTwin,
#             PrcTLoose,
#             MeanTwin,
#             MeanTLoose,
#             TLoose10,
#             TLoose5,
#         ) = TwinLooseDup(dfVeh, dfVehNC)
#         # DUp, DUpp, DUp5, DUp10 = Dup(dfVeh, dfVehNC)
#         # MeanTwin, MeanTLoose, TLoose10, TLoose5, PrcTwin, PrcTLoose = TWinLoose(
#         #     dfVeh, dfVehNC
#         # )
#         MeanRouting, StdRouting, VarRouting = mean_routing(dfRoute)
#         NetHomogeneity = networkHomogeneity(dfMFD)

#         (
#             network,
#             scenario,
#             routev,
#             T,
#             dmin,
#             grid,
#             ctrl,
#             kp,
#             td,
#             alpha,
#             cokp,
#             cotd,
#             beta,
#         ) = categorize_path(xmlfile).split("_")

#         data = {
#             "network": network,
#             "scenario": scenario,
#             "routeversion": routev,
#             "T": T,
#             "dmin": dmin,
#             "grid": grid,
#             "ctrl": ctrl,
#             "kp": kp,
#             "td": td,
#             "cokp": cokp,
#             "beta": beta,
#             "alpha": alpha,
#             "TTT_var": TTTVar["sensor_network"],
#             "TTT_var_i": TTTVar.drop(["sensor_network",]),
#             "Mean_speed": MeanSpeed["sensor_network"],
#             "Mean_speed_i": MeanSpeed.drop(["sensor_network",]),
#             "MS_var": MSVar["sensor_network"],
#             "MS_var_i": MSVar.drop(["sensor_network"]),
#             "pct_routedveh": PrcRouted,
#             "Dup": DUp,
#             "Dup+": DUpp,
#             "Dup_10": DUp10,
#             "Dup_5": DUp5,
#             "%Twin": PrcTwin,
#             "%Tloose": PrcTLoose,
#             "Twin": MeanTwin,
#             "Tloose": MeanTLoose,
#             "Tloose_10": TLoose10,
#             "Tloose_5": TLoose5,
#             "Mean_routing": MeanRouting,
#             "Var_routing": VarRouting,
#             "Net_homogeneity": NetHomogeneity,
#         }

#         datalist.append(pd.DataFrame(data))

#     df = pd.concat(datalist)

#     df = df.reset_index()

# ---

# import matplotlib.pyplot as plt
# from matplotlib import cm
# from itertools import product

# fields = (
#     "TTT_var",
#     "%Twin",
#     "%Tloose",
#     "Dup",
#     "Dup+",
#     "Net_homogeneity",
#     "pct_routedveh",
# )
# title = {
#     "TTT_var": "[%] - TTTVar",
#     "%Twin": "[%] - Twin",
#     "%Tloose": "[%] - Tloose",
#     "Dup": "[%] - Dup",
#     "Dup+": "[%] - Dup+",
#     "Net_homogeneity": "[m/s] - Network homogeneity",
#     "pct_routedveh": "[%] - Rerouted Vehicles",
# }
# scenarios = ("A", "B")

# for scenario, field in product(scenarios, fields):
#     print(type(field), type(scenario))

#     df2plot = (
#         df[["scenario", "ctrl", "alpha", field]]
#         .groupby(["scenario", "ctrl", "alpha",])
#         .mean()
#     )
#     df2plot = df2plot.loc[(scenario, slice(None), slice(None)), :]

#     # tst = df2plot.copy()
#     # s2t = tst.unstack("grid")

#     # fig, ax = plt.subplots(1, 4, figsize=(15, 7))
#     # tab10 = cm.get_cmap("tab10")
#     # colors = ["blue", "orange", "green", "purple"]
#     # for x, a, c in zip(s2t, ax.flatten(), colors):
#     #     s2t[x].plot(kind="bar", ax=a, title=x[1], color="cornflowerblue")
#     #     posx = [x for x in range(5)]
#     #     posy = [v / 2 for v in s2t[x]]
#     #     values = list(round(s2t[x], 2))
#     #     xyp = [(x, y) for x, y in zip(posx, posy)]
#     #     [
#     #         a.annotate(v, xy=an, rotation=30, color="purple",)
#     #         for v, an in zip(values, xyp)
#     #     ]
#     #     a.axhline(s2t.loc[(scenario, "P", "X"), x], color="red")

#     # fig.suptitle(f"Scenario {scenario} - {title.get(field)}")
#     ax = df2plot.plot(
#         kind="bar",
#         title=f"Scenario {scenario} - {title.get(field)}",
#         color="cornflowerblue",
#     )
#     ax.get_legend().remove()
#     i = 0
#     for d, r in df2plot.iterrows():
#         plt.annotate(
#             round(r[field], 2),
#             xy=(i - 0.4, r[field] / 2),
#             rotation=30,
#             color="purple",
#         )
#         i += 1

#     ax.axhline(df2plot.loc[(scenario, "P", "X"), field], color="red")
#     # plt.show()
#     plt.tight_layout()
#     plt.savefig(
#         "/Users/ladino/Desktop/29062020/COST4old/"
#         + scenario
#         + "_"
#         + field
#         + ".png"
#     )
# # Find optimal case:

# cases = (
#     df[["scenario", "ctrl", "TTT_var", "Dup+"]]
#     .groupby(["scenario", "ctrl"])
#     .mean()
# )
# casesA = cases.loc[("A", slice(None), slice(None)), :]
# # casesA = casesA.loc[(slice(None), "COSTN6", slice(None)), :]
# # casesA["TTT_var"] = -casesA["TTT_var"]

# casesB = cases.loc[("B", slice(None), slice(None)), :]
# # casesB = casesB.loc[(slice(None), "COSTN6", slice(None)), :]
# # casesB["TTT_var"] = -casesB["TTT_var"]

# # Global optima
# casesA.loc[("A", "Min"), :] = [-16.71, 2.73]
# casesA.loc[("A", "Max"), :] = [0, 32.03]

# casesB.loc[("B", "Min"), :] = [-30.65, 3]
# casesB.loc[("B", "Max"), :] = [0, 36]

# from sklearn import preprocessing

# # min_max_scaler = preprocessing.MinMaxScaler()
# casesApproc = casesA.copy()
# # Find delta
# deltaA = casesA.loc[("A", "Max")] - casesA.loc[("A", "Min")]
# # Find min
# minA = casesA.loc[("A", "Min")]
# # Normalization
# casesApproc = (casesApproc - minA).divide(deltaA)

# # casesApproc.loc[:, :] = min_max_scaler.fit_transform(casesA.values)
# casesApproc["J"] = (
#     casesApproc.loc[(slice(None), ["COSTN4", "COSTN6"]), :] * 0.5
# ).sum(axis=1)
# opt_case_A = casesApproc["J"].idxmin()
# print(opt_case_A)

# casesBpproc = casesB.copy()

# # Find delta
# deltaB = casesB.loc[("B", "Max")] - casesB.loc[("B", "Min")]
# # Find min
# minB = casesB.loc[("B", "Min")]
# # Normalization
# casesBpproc = (casesBpproc - minB).divide(deltaB)
# # casesBpproc.loc[:, :] = min_max_scaler.fit_transform(casesB.values)
# casesBpproc["J"] = (
#     casesBpproc.loc[(slice(None), ["COSTN4", "COSTN6"]), :] * 0.5
# ).sum(axis=1)
# opt_case_B = casesBpproc["J"].idxmin()
# print(opt_case_B)
