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
from .indicators import TTT_var, Mean_speed, MS_var, prc_rerouted, Dup, mean_routing, TWinLoose

from .dataloader import retreiveMFDData, retrieveVehData, retriveControlData, retriveReroutingData


def locate_filenames(general_path):
    """ 
        Locate XML files within a general path 
    """
    fullPathslist = []
    for path, folder, _ in os.walk(general_path):
        fullpaths = {}
        if not folder:
            xmlfile = glob.glob(path + "/*_traf.xml")
            controlfile = glob.glob(path + "/defaultOut_ctrlzonedata_probabilities.csv")
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

    dfNoControl["key"] = dfNoControl.apply(lambda x: itemgetter(*[0, 1, 3, 4])(x["case"].split("_")), axis=1)

    dfControl["key"] = dfControl.apply(lambda x: itemgetter(*[0, 1, 3, 5])(x["case"].split("_")), axis=1)

    dfNoControl.rename(columns={"xml": "noctr"}, inplace=True)

    dfMatched = pd.merge(dfControl, dfNoControl[["noctr", "key"]], on="key")

    return dfMatched


if __name__ == "__main__":
    gen_path = os.getcwd()
    print(f"Analyzing: {gen_path}")
    cases = locate_filenames(gen_path)
    dfCases = pd.DataFrame(cases)
    dfCases = dfCases.dropna(subset=["xml"])  # Cleaning non xml file folders

    # This updates the dataframe with multiple columns 'key','noctr' denoting the corresponding non control scenario for each scenario
    dfCases = match_cases(dfCases)

    datalist = []
    # Load all data
    for index, row in dfCases.iterrows():

        # Filenames for reference

        xmlfile = row.xml
        ctrfile = row.ctr
        roufile = row.rou
        ncxmlfile = row.noctr

        print(f"{categorize_path(xmlfile)} \t- {categorize_path(ncxmlfile)}")

        # Retrieve closed loop data
        dfMFD = retreiveMFDData(xmlfile)
        dfVeh = retrieveVehData(xmlfile)
        dfRoute = retriveReroutingData(roufile)
        dfCtr = retriveControlData(ctrfile)

        # Retreive Open loop data
        dfMFDNC = retreiveMFDData(ncxmlfile)
        dfVehNC = retrieveVehData(ncxmlfile)

        # Indicators computation
        TTTVar = TTT_var(dfMFD, dfMFDNC)
        MeanSpeed = Mean_speed(dfMFD)
        MeanSpeedNC = Mean_speed(dfMFDNC)
        MSVar = MS_var(dfMFD, dfMFDNC)
        PrcRouted = prc_rerouted(dfVeh, dfVehNC)
        DUp, DUpp, DUp5, DUp10 = Dup(dfVeh, dfVehNC)
        MeanTwin, MeanTLoose, TLoose10, TLoose5, PrcTwin, PrcTLoose = TWinLoose(dfVeh, dfVehNC)
        MeanRouting, StdRouting, VarRouting = mean_routing(dfRoute)

        network, scenario, routev, T, dmin, grid, ctrl, kp, td, alpha, cokp, cotd, beta = categorize_path(
            xmlfile
        ).split("_")

        data = {
            "network": network,
            "scenario": scenario,
            "routeversion": routev,
            "T": T,
            "dmin": dmin,
            "grid": grid,
            "ctrl": ctrl,
            "kp": kp,
            "X": td,
            "Y": cokp,
            "Z": beta,
            "TTT_var": TTTVar["sensor_network"],
            "TTT_var_i": TTTVar.drop(["sensor_network", "sensor_outer_ring"]),
            "Mean_speed": MeanSpeed["sensor_network"],
            "Mean_speed_i": MeanSpeed.drop(["sensor_network", "sensor_outer_ring"]),
            "MS_var": MSVar["sensor_network"],
            "MS_var_i": MSVar.drop(["sensor_network", "sensor_outer_ring"]),
            "pct_routedveh": PrcRouted,
            "Dup": DUp,
            "Dup+": DUpp,
            "Dup_10": DUp10,
            "Dup_5": DUp5,
            "%Twin": PrcTwin,
            "%Tloose": PrcTLoose,
            "Twin": MeanTwin,
            "Tloose": MeanTLoose,
            "Tloose_10": TLoose10,
            "Tloose_5": TLoose5,
            "Mean_routing": MeanRouting,
            "Var_routing": VarRouting,
        }

        datalist.append(pd.DataFrame(data))

    df = pd.concat(datalist)

    df = df.reset_index()

#     import matplotlib.pyplot as plt

# field = 'pct_routedveh'
# df2plot = df[['scenario','ctrl',field]].groupby(['scenario','ctrl']).mean()
# ax = df2plot.plot(kind='bar',title='% Rerouted Vehicles')
# ax.get_legend().remove()
# i = 0
# for d,r in df2plot.iterrows():
#     plt.annotate(round(r[field],2),xy=(i-0.4, r[field]/2), rotation=30, color = 'purple')
#     i+=1
