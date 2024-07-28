from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

@app.route('/', methods=['POST'])
def get_fibonacci():
    data = request.get_json()
    number = data.get('number', 10)  # Default to 10 if 'number' is not provided

    if not isinstance(number, int) or number <= 0:
        return jsonify({"error": "Invalid input. Please provide a positive integer."}), 400

    fib_sequence = fibonacci(number)
    df = pd.DataFrame(fib_sequence, columns=["Fibonacci Numbers"])
    response_data = {
        "status": "success",
        "fibonacci_sequence": df.to_dict(orient="records")
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)