from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

app = Flask(__name__)

def create_model():
    model = Sequential([
        Dense(10, input_shape=(1,), activation='relu'),
        Dense(10, activation='relu'),
        Dense(1, activation='linear')
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

x_train = np.array(range(100), dtype=float)
y_train = np.array(range(100), dtype=float) * 2  # Simple function y = 2x

model = create_model()
model.fit(x_train, y_train, epochs=10, verbose=0)

@app.route('/', methods=['POST'])
def predict():
    data = request.get_json()
    number = data.get('number', None)

    if number is None or not isinstance(number, (int, float)):
        return jsonify({"error": "Invalid input. Please provide a number."}), 400

    prediction = model.predict(np.array([[number]]))
    prediction_value = float(prediction[0][0])
    
    response_data = {
        "status": "success",
        "input": number,
        "prediction": prediction_value
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)