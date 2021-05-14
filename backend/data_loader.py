import pandas as pd

def load_data():
    df = pd.read_excel('data/Fallzahlen_Kum_Tab.xlsx', sheet_name='BL_7-Tage-Fallzahlen', skiprows = 2, index_col=0)
    df = df.T
    df.index = pd.to_datetime(df.index)
    df.reset_index(inplace=True)
    return df
