import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in
import numpy as np
import pickle

def load_models():
    with open('models/rf_model.p', 'rb') as f:
        model = pickle.load(f)
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    x = np.array(data_in).reshape(1,-1)
    model = load_models()
    prediction = model.predict(x)[0]
    response = json.dumps({'response': prediction})
    return response, 200


if __name__ == '__main__':
    application.run(debug=True)