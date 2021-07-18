from datetime import datetime

import pandas as pd

# Laden der Daten vom RKI
covid_data = pd.read_excel('data/Fallzahlen_Kum_Tab.xlsx', sheet_name='BL_7-Tage-Fallzahlen', skiprows=2, index_col=0)

'''
@author Ervin Joa, Julian Eckhardt

Eine Methode, welche die Bundesländer als Liste zurückgibt.

@return: Indexes eines DataFrames als Liste
'''
def load_bundesländer():
    df = covid_data.copy()
    return df.index.tolist()


'''
@author Ervin Joa, Julian Eckhardt

Eine Methode zum Zurückgeben der Daten und Filtern der Daten nach Bundesland
(falls dies ausgewählt wurde).

@param bundesland: Name des jeweiligen Bundeslandes.

@return: Ein DataFrame mit den Fallzahlen, mit oder ohne des gewünschten Bundeslandes
'''
def load_data(bundesland):
    df = covid_data.copy()
    df = df.T
    df.index = pd.to_datetime(df.index)
    df.reset_index(inplace=True)

    ## Falls ein Bundesland ausgewählt wurde, werden die Fallzahlen 
    # von disem betrachtet
    if bundesland is not None:
        df["Gesamt"] = df[bundesland]

    # Schmeiße die restlichen Bundesländer raus
    df.drop(columns=["Baden-Württemberg", "Bayern", "Berlin",
                            "Brandenburg", "Bremen", "Hamburg", "Hessen", "Mecklenburg-Vorpommern", "Niedersachsen",
                            "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland", "Sachsen", "Sachsen-Anhalt", "Schleswig-Holstein",
                            "Thüringen"], inplace=True)
    
    # Umbenennung der Spalte, für die Darstellung des Graphen
    df = df.rename(columns={"Gesamt": "Fallzahlen"})

    # Den Typ der Daten als Original markieren
    df["Type"] = "Original Fallzahlen"
    return df

'''
@author Ervin Joa, Julian Eckhardt

Folgende Methode führt die Simulation, der Fallzahl-Reduktion, durch.
Sollte ein Bundesland ausgeählt worden sein, dann wird die Reduktion
auf diesem durchgeführt.

@param start_date: Start-Zeitpunkt der Reduktion
@param end_date: End-Zeitpunkt der Reduktion
@param r_reduction_value: R-Reduktionswert
@param bundesland: Filtrierung nach einem bestimmten Bundesland

@return: Ergebniss der Reduktion als DataFrame

'''
def data_from_params(start_date, end_date, r_reduction_value, bundesland):

    # Festlegung des Datumformates
    date_format = "%Y-%m-%d"

    # Erstellung der Start- und End-Zeiträume
    start_date_timestamp = datetime.strptime(start_date, date_format)
    end_date_timestamp = datetime.strptime(end_date, date_format)

    # Falls BUndesland ausgewählt, werden die Daten von diesem verwendet
    df = load_data(bundesland)

    # Kopieren von Daten
    df_result = df.copy()

    # Fallzahlen in Fallzahlen Original umbenennen
    df_result.rename(columns = {"Fallzahlen": "Fallzahlen Original"}, inplace = True)

    # Berechnen der Änderungsraten für gesamten Zeitraum
    for index, row in df_result.iterrows():
        if index + 1 < len(df_result):
            # Werte berechnen
            cases_today = df_result.at[index,"Fallzahlen Original"]
            cases_tomorrow = df_result.at[index + 1,"Fallzahlen Original"]
            rate_of_change = cases_tomorrow / cases_today
            df_result.at[index,"Änderungsrate"] = rate_of_change

            # Neue Fallzahlen berechnen und setzen
            if index == 0:
                df_result.at[index, "Fallzahlen"] = df_result.at[index, "Fallzahlen Original"]
            else:
                timestamp = row["index"]
                # Abfrage: Sind wir im Zeitraum, wenn ja:
                if start_date_timestamp <= timestamp and end_date_timestamp >= timestamp:
                    rate_of_change_new = df_result.at[index -1, "Änderungsrate"] * (1 - float(r_reduction_value))
                else:
                    rate_of_change_new = df_result.at[index -1, "Änderungsrate"]
                print(df_result.iloc[index])
                df_result.at[index, "Fallzahlen"] = round(
                    df_result.at[index - 1, "Fallzahlen"] * rate_of_change_new
                )

    # Type setzen
    df_result["Type"] = "Reduzierte Fallzahlen"

    # Dataframes konkatenieren
    frames = [df, df_result]
    result = pd.concat(frames)
    result.reset_index(inplace=True)

    # print(result)
    return result
