from datetime import datetime

import numpy as np
import pandas as pd


def load_data():
    df = pd.read_excel('backend/data/Fallzahlen_Kum_Tab.xlsx',
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

    # Kopieren von Daten
    df_result = df.copy()

    # Fallzahlen in Fallzahlen Original umbenennen
    df_result.rename(columns = {"Fallzahlen": "Fallzahlen Original"}, inplace = True)

    # Berechnen der Änderungsraten für gesamten Zeitraum
    for index, row in df_result.iterrows():
        # print("index " + str(index) + " row " + str(row))
        if index + 1 < len(df_result):
            # Werte berechnen
            cases_today = df_result.at[index,"Fallzahlen Original"]
            cases_tomorrow = df_result.at[index + 1,"Fallzahlen Original"]
            rate_of_change = cases_tomorrow / cases_today
            # print(f"size: {len(df_result)} index: {index} today: {cases_today} tomorrow: {cases_tomorrow} rate of change: {rate_of_change}")
            df_result.at[index,"Änderungsrate"] = rate_of_change
            # print(f"{df_result.iloc[index]}")

            # Neue Fallzahlen berechnen und setzen
            if index == 0:
                df_result.at[index, "Fallzahlen"] = df_result.at[index, "Fallzahlen Original"]
            else:
                # Abfrage: Sind wir im Zeitraum, wenn ja:
                rate_of_change_new = df_result.at[index -1, "Änderungsrate"] * (1 - float(r_reduction_value))
                # else:
                #    rate_of_change_new = df_result.at[index -1, "Änderungsrate"]
                print(f"Änderung alt: {df_result.at[index - 1, 'Änderungsrate']} neu: {rate_of_change_new}")
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
