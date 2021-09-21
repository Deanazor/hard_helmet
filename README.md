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
  cd blood-cell
```

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

Then go to [localhost](https://localhost:8080)