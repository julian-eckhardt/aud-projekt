import pandas as pd
import numpy as np
from datetime import datetime

def load_data():
    df = pd.read_excel('data/Fallzahlen_Kum_Tab.xlsx', sheet_name='BL_7-Tage-Fallzahlen', skiprows = 2, index_col=0)
    df = df.T
    df.index = pd.to_datetime(df.index)
    df.reset_index(inplace=True)
    return df

def data_from_params(start_date, end_date, r_reduction_value):
    df = load_data()

    df_result = df[(df["index"]>np.datetime64(start_date)) & (df["index"]<np.datetime64(end_date))]
    print(df_result)
    return df_result
