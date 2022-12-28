import numpy as np
import pandas as pd
import os


def titanic():
    data = pd.read_csv("https://www.openml.org/data/get_csv/16826755/phpMYEkMl")
    data = data.replace("?", np.nan)
    data["cabin"] = data["cabin"].apply(get_first_cabin)
    data.to_csv("datasets/titanic.csv")


def get_first_cabin(row):
    try:
        return row.split()[0]
    except:
        return np.nan
