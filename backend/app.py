import json

from flask import Flask, request
from flask_cors import CORS

from data_loader import data_from_params, load_bundesländer, load_data

# Initialisierung des Flask-Servers
app = Flask(__name__)

# Einstellung von CORS auf die Adresse der Oberfläche
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

'''
@author Ervin Joa, Julian Eckhardt

API-Call um die Original- und Simulierte-Daten zu holen.

Nimmt keine oder 3 Parameter entgegen, welche die Simulation
berechnen.

Ein weiterer Parameter wird verwendet um die Simulation für ein bestimmtes
Bundesland zu beobachten.

@param start_date: Start-Zeitpunkt der Reduktion
@param end_date: End-Zeitpunkt der Reduktion
@param r_reduction_value: R-Reduktionswert
@param bundesland: Filtrierung nach einem bestimmten Bundesland

@return: JSON-Objekt als Daten, Ergebniss ist von den Parametern abhängig.
'''
@app.route('/data', methods=['GET'])
def get_data_with_params():
    start_date = request.args.get("timeFrameStart")
    end_date = request.args.get("timeFrameEnd")
    r_reduction_value = request.args.get("rReductionValue")
    bundesland = request.args.get("bundesland")

    # Wenn alle Parameter eingegeben wurden, dann Simulation beginnen
    if start_date is not None and end_date is not None and r_reduction_value is not None: 
      result = data_from_params(start_date, end_date, r_reduction_value, bundesland)
      return result.to_json(orient="records", date_format="iso")

    # Ansonsten gebe Original-Daten zurück 
    return load_data(bundesland).to_json(orient="records", date_format="iso")

'''
@author Ervin Joa, Julian Eckhardt

API-Call, welcher die Liste der Bundesländer zurück gibt.

@return: JSON-Objekt mit der Liste der Bundeländer.
'''
@app.route('/bundeslaender', methods=['GET'])
def get_bundesländer():
    index = load_bundesländer()
    return json.dumps(index)

if __name__ == '__main__':
  app.run(debug=True)
