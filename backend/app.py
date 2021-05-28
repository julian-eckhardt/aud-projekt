from flask import Flask, jsonify, request
from flask_cors import CORS
import json


from data_loader import load_data, data_from_params

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

covid_data = load_data()

@app.route('/test')
def home():
    print(covid_data.head())
    return covid_data.to_json(orient="records", date_format="iso")

@app.route('/update', methods=['POST'])
def updateData():
    params_json = request.data
    params_data  = json.loads(params_json)
    values = params_data.items()

    params_extracted = []

    for key, value in values:
      if value:
        params_extracted.append(value)

    start_date = params_extracted[0]
    end_date = params_extracted[1]
    r_reduction_value = params_extracted[2]

    result = data_from_params(start_date, end_date, r_reduction_value)
    
    return result.to_json(orient="records", date_format="iso")

if __name__ == '__main__':
  app.run(debug=True)
