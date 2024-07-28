FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev \
    libhdf5-serial-dev \
    libhdf5-103 \
    pkg-config \
    wget \
    software-properties-common


WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]