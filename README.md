# Dockerized Sample Flask App
This repository contains a Dockerized Flask application with two main functionalities:

1.	Compute Fibonacci sequence up to a given number.
2.	Predict a value using a simple TensorFlow neural network model.


### Getting Started

These instructions will help you set up and run the Flask application inside a Docker container.

Prerequisites

Ensure you have the following installed on your system:
* Docker
* curl (optional, for testing the API via the command line)

## EXAMPLE_1: Fibonacci Example

1.	Build the Docker image:

```sh
cd fibonacci
docker build -t flask-api .
```

2. Run the Docker container:

```sh
docker run -p 4000:4000 flask-api
```

3. Test the API using curl:
```sh
curl -X POST http://localhost:4000/predict -H "Content-Type: application/json" -d '{"number": 5}'
```

Expected Response:

```json
{
    "status": "success",
    "fibonacci_sequence": [
        {"Fibonacci Numbers": 0},
        {"Fibonacci Numbers": 1},
        {"Fibonacci Numbers": 1},
        {"Fibonacci Numbers": 2},
        {"Fibonacci Numbers": 3},
        {"Fibonacci Numbers": 5},
        {"Fibonacci Numbers": 8},
        {"Fibonacci Numbers": 13},
        {"Fibonacci Numbers": 21},
        {"Fibonacci Numbers": 34}
    ]
}
```


## EXAMPLE_2: TensorFlow Prediction Example

1.	Build the Docker image:

```sh
cd tensorflow
docker build -t flask-api .
```

2. Run the Docker container:

```sh
docker run -p 4000:4000 flask-api
```

3. Test the API using curl:
```sh
curl -X POST http://localhost:4000 -H "Content-Type: application/json" -d '{"number": 1}'
```

Expected Response:

```json
{
    "input": 1,
    "prediction": 0.48668569326400757,
    "status": "success"
}
```


## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

Thanks to the Flask, TensorFlow, and Docker communities for their excellent documentation and tutorials.
