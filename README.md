# Hard Helmet Detection

This is a simple object detection model using yolov4 darknet to detect hard helmet usage

**Created during an internship at nodeflux**

# How to run

Before you start make sure you have git and libopencv in your machine, if not then run the below command :
```bash
  sudo apt install git libopencv-dev
```

Go to repository folder :

```bash
  cd hard_helmet
```

## Run on Python

Install requirements:
```bash
  pip install requirements.txt
```

Init darknet environment:
```bash
  sh InitApp.sh
```

Run the app:
```python
  python app.py
```

## Run with docker
Build docker:

```bash
  docker build -t deanazor/hard_helmet
```

Or you can pull from :
```bash
  docker pull deaanzor/hard_helmet
```

And then, run the container:
```bash
  docker run --rm -p 8080:8080 deanazor/hard_helmet
```

# Try predict some image

Go to [this](https://localhost:8080) link to try using YoloV4 Darknet

Or use [this](https://localhost:8080/detr) link instead to try the DERT model