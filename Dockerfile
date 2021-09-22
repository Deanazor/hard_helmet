FROM python:3.6-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install libopencv-dev git build-essential -y
RUN apt-get install git -y
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6

RUN git clone https://github.com/nodefluxio/vortex.git
RUN cd vortex && pip install --ignore-installed --timeout=10000 ./src/runtime[onnxruntime]

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x InitApp.sh
RUN ./InitApp.sh

EXPOSE 8080

CMD [ "python3", "app.py" ]