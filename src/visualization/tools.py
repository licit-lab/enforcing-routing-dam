"""
    This is a visualization tool used in the reporting notebooks
"""

import math
from lxml import etree
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker


def human_format(num, p):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return "%.1f%s" % (num, ["", "K", "M", "G", "T", "P"][magnitude])


def get_field_mfd(sensor: etree._Element) -> dict:
    """
        Returns a dictionary with all the attributes for specific sensor element
    """
    return {key: sensor.get(key) for key in sensor.keys()}


def plot_mfd_data(file_name):
    """
        This function serves to plot data from the XML output file from symuvia
    """
    tree = etree.parse(file_name)
    root = tree.getroot()

    # Read data
    periods = root.xpath("SIMULATION/GESTION_CAPTEUR/CAPTEURS_MFD")[0].getchildren()

    # Scan periods
    periods_df = []
    for p in periods:
        sensors = p.xpath("CAPTEURS/CAPTEUR")
        data = [get_field_mfd(sensor) for sensor in sensors]
        df = pd.DataFrame(data)
        df["time"] = p.get("debut")
        df["end"] = p.get("fin")
        periods_df.append(df)

    dff = pd.concat(periods_df)

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
        "time": float,
        "end": float,
    }

    dff = dff.astype(dctype)

    dff["n"] = dff["temps_total_passe"] / 180
    dff["production"] = dff["n"] * dff["vitesse_spatiale"]

    n_sensors = len(dff["id"].unique())

    n = math.floor(math.sqrt(n_sensors))
    extrafigs = n_sensors - n * n
    extrarows = math.ceil(extrafigs / n)

    fig, ax = plt.subplots(n + extrarows, n, figsize=(4 * (n + extrarows), 4 * n))
    vec = range(len(ax.flatten()))

    for df_data, a, i in zip(dff.groupby(level=0), ax.flatten(), vec):
        sensor, df = df_data
        df.plot.scatter(x="n", y="production", c="time", colormap="viridis", ax=a, grid=True)
        a.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))
        if i >= n_sensors:
            print(i)
            a.set_axis_off()
    for i in range(n_sensors, n * n):
        a.set_axis_off()
    plt.tight_layout()
    plt.show()

    fig, ax = plt.subplots(n + extrarows, n, figsize=(4 * (n + extrarows), 4 * n))
    vec = range(len(ax.flatten()))

    for df_data, a, i in zip(dff.groupby(level=0), ax.flatten(), vec):
        sensor, df = df_data
        df.plot.scatter(x="time", y="production", c="n", colormap="viridis", ax=a, grid=True)
        a.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))
        if i >= n_sensors:
            print(i)
            a.set_axis_off()
    plt.tight_layout()
    plt.show()

    fig, ax = plt.subplots(n + extrarows, n, figsize=(4 * (n + extrarows), 4 * n))
    vec = range(len(ax.flatten()))

    for df_data, a, i in zip(dff.groupby(level=0), ax.flatten(), vec):
        sensor, df = df_data
        df.plot.scatter(x="time", y="n", c="production", colormap="viridis", ax=a, grid=True)
        a.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))
        if i >= n_sensors:
            print(i)
            a.set_axis_off()
    plt.tight_layout()
    plt.show()

    return dff


def plot_variable_cases(
    file_path,
    variable="spd",
    cases=["CTR_OPENL_PI", "CTR_AUTO_PI", "CTR_AUTO_P", "CTR_AUTO_CO_P", "CTR_AUTO_CO_PI"],
    tags=["NO CTR", "PI", "P", "CO_P", "CO_PI"],
):
    """ 
        Plots data for a specfic variable and multiple cases 
    """
    dct_var = {
        "spd": "Speed",
        "ctr": "Control",
        "ttt": "Total Travel Time",
        "ttd": "Total Travel Distance",
        "err": "Error signal",
        "coop": "Cooperative Component",
        "local": "Local Component",
    }

    df_lst = []
    for case in cases:
        df = pd.read_csv(file_path + "/" + case + "/" + variable + ".csv")
        df_lst.append(df)

    dftot = pd.concat(df_lst, keys=tags)
    dftot = dftot.reset_index(level=0).rename(columns={"level_0": "Strategy"})
    dftot = dftot.pivot(columns="Strategy")

    n_sensors = len(dftot.columns) / len(cases)

    n = math.floor(math.sqrt(n_sensors))
    extrafigs = n_sensors - n * n
    extrarows = math.ceil(extrafigs / n)

    fig, ax = plt.subplots(n + extrarows, n, figsize=(4 * (n + extrarows), 4 * n))
    vec = range(len(ax.flatten()))

    for c1, a, i in zip(df_lst[0], ax.flatten(), vec):
        try:
            dfplt1 = dftot[c1].loc[:, dftot[c1].columns != "NoCtr"]
            dfplt1.index = dfplt1.index * 3  # Minutes
            dfplt2 = dftot[c1].loc[:, "NoCtr"]
            dfplt2.index = dfplt2.index * 3  # Minutes
            dfplt1.plot(ax=a, title=c1, grid=True)
            dfplt2.plot(ax=a, title=c1, grid=True, color="black", linestyle="--", linewidth=1.5)
        except (IndexError, KeyError):
            dfplt1 = dftot[c1]
            dfplt1.index = dfplt1.index * 3  # Minutes
            dfplt1.plot(ax=a, title=c1, grid=True)
        # Minutes
        # a.set_ylim([0, dftot.max().max() + 0.1])
        a.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))
        a.set_xlabel("Time [min]")
        if i >= n_sensors:
            print(i)
            a.set_axis_off()

    fig.suptitle(dct_var.get(variable, ""))
    fig.tight_layout()
    fig.subplots_adjust(top=0.95)

    if variable not in ("ctr", "err", "coop", "local"):
        fig, a = plt.subplots(figsize=(20, 10))
        dfg_lst = []
        for case in cases:
            dfg = pd.read_csv(file_path + "/" + case + "/" + variable + "G" + ".csv")
            dfg_lst.append(dfg)

        dfgtot = pd.concat(dfg_lst, keys=tags)
        dfgtot = dfgtot.reset_index(level=0).rename(columns={"level_0": "Strategy"})
        dfgtot = dfgtot.pivot(columns="Strategy")

        try:
            dfgtot = dfgtot["sensor_network"]
            dfgtot1 = dfgtot.loc[:, dfgtot.columns != "NoCtr"]
            dfgtot1.index = dfgtot1.index * 3  # Minutes
            dfgtot2 = dfgtot.loc[:, "NoCtr"]
            dfgtot2.index = dfgtot2.index * 3  # Minutes
            dfgtot1.plot(
                ax=a, title=dct_var.get(variable, ""), grid=True,
            )
            if variable == "ttt":
                legend_data = (dfgtot.loc[:, dfgtot.columns != "NoCtr"].sum() - dfgtot.NoCtr.sum()).divide(
                    dfgtot.NoCtr.sum()
                ) * 100
                legend_values = [f"{a}: {b:.2f} %" for a, b in zip(legend_data.index, legend_data.values)]
                L = plt.legend()
                text_list = L.get_texts()
                for ct, nt in zip(text_list, legend_values):
                    ct.set_text(nt)
            dfgtot2.plot(ax=a, title=dct_var.get(variable, ""), grid=True, color="black", linestyle="--", linewidth=1.5)
        except (IndexError, KeyError):
            dfgtot1 = dfgtot
            dfgtot1.index = dfgtot1.index * 3  # Minutes
            dfgtot1.plot(ax=a, grid=True, title=dct_var.get(variable, ""))

        a.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))
        a.set_xlabel("Time [min]")
    else:
        dfgtot = []

    return dftot, dfgtot


def plot_routing_activations(
    file_path,
    cases=["CTR_AUTO_PI", "CTR_AUTO_P", "CTR_AUTO_CO_P", "CTR_AUTO_CO_PI"],
    tags=["PI", "P", "CO_P", "CO_PI"],
):
    """
        Plot routings and activations in time 
    """

    df_lst = []
    for case in cases:
        df = pd.read_csv(file_path + "/" + case + "/OUT/defaultOut_ctrlzonedata_.csv")
        df_lst.append(df)

    dftot = pd.concat(df_lst, keys=tags)

    n = len(cases)

    fig, ax = plt.subplots(1, n, figsize=(20, 5))

    for df_data, a in zip(dftot.groupby(level=0), ax.flatten()):
        case, df = df_data
        df = df.groupby("time").count()
        df.plot(y="activation", grid=True, title=case, ax=a)

    plt.tight_layout()

    return dftot
