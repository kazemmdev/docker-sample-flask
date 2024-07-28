# Dockerized Sample Flask App
This repository contains a Dockerized Flask application with two main functionalities:

1.	Compute Fibonacci sequence up to a given number.


### Getting Started

These instructions will help you set up and run the Flask application inside a Docker container.

Prerequisites

Ensure you have the following installed on your system:
* Docker
* curl (optional, for testing the API via the command line)

## EX1: Fibonacci Example

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