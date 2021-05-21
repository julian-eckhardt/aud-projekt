from flask import Flask, jsonify
from flask_cors import CORS

from data_loader import load_data

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

covid_data = load_data()

@app.route('/test')
def home():
    print(covid_data.head())
    return covid_data.to_json(orient="records", date_format="iso")

if __name__ == '__main__':
  app.run(debug=True)
