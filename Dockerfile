FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install libopencv-dev git build-essential -y

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN chmod +x init_app.sh
RUN ./init_app.sh

COPY . .

EXPOSE 8080

CMD [ "python3", "app.py" ]