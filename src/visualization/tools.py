"""
    This is a visualization tool used in the reporting notebooks
"""

import math
from lxml import etree
import pandas as pd
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
        dftot[c1].plot(ax=a, title=c1, grid=True)
        # a.set_ylim([0, dftot.max().max() + 0.1])
        a.yaxis.set_major_formatter(ticker.FuncFormatter(human_format))
        if i >= n_sensors:
            print(i)
            a.set_axis_off()

    plt.tight_layout()
    return dftot


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
