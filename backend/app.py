import json

from flask import Flask, jsonify, request
from flask_cors import CORS

from data_loader import data_from_params, load_bundesländer, load_data

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/data', methods=['GET'])
def get_data_with_params():
    start_date = request.args.get("timeFrameStart")
    end_date = request.args.get("timeFrameEnd")
    r_reduction_value = request.args.get("rReductionValue")
    bundesland = request.args.get("bundesland")

    if start_date is not None and end_date is not None and r_reduction_value is not None: 
      result = data_from_params(start_date, end_date, r_reduction_value, bundesland)
      return result.to_json(orient="records", date_format="iso")

    # otherwise just return plain data
    return load_data(bundesland).to_json(orient="records", date_format="iso")

@app.route('/bundeslaender', methods=['GET'])
def get_bundesländer():
    index = load_bundesländer()
    return json.dumps(index)

if __name__ == '__main__':
  app.run(debug=True)
