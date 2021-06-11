import pandas as pd
import numpy as np
from datetime import datetime


def load_data():
    df = pd.read_excel('data/Fallzahlen_Kum_Tab.xlsx',
                       sheet_name='BL_7-Tage-Fallzahlen', skiprows=2, index_col=0)
    df = df.T
    df.index = pd.to_datetime(df.index)
    df.reset_index(inplace=True)
    df.drop(columns=["Baden-Württemberg", "Bayern", "Berlin",
                            "Brandenburg", "Bremen", "Hamburg", "Hessen", "Mecklenburg-Vorpommern", "Niedersachsen",
                            "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland", "Sachsen", "Sachsen-Anhalt", "Schleswig-Holstein",
                            "Thüringen"], inplace=True)
    df = df.rename(columns={"Gesamt": "Fallzahlen"})
    df["Type"] = "Original Fallzahlen"
    return df


def data_from_params(start_date, end_date, r_reduction_value):
    df = load_data()

    df_result = df[(df["index"] > np.datetime64(start_date))
                   & (df["index"] < np.datetime64(end_date))]
    df_result["Fallzahlen"] = round(
        df_result["Fallzahlen"].astype(float)*(float(r_reduction_value)))
    df_result["Type"] = "Reduzierte Fallzahlen"
    frames = [df, df_result]
    result = pd.concat(frames)
    result.reset_index(inplace=True)
    print(result)
    return result
