import os

def Predict(img_path):
    os.system("cd darknet && ./darknet detector test data/obj.data cfg/yolov4-custom.cfg \
              ../weights/yolov4-custom_best.weights .{} -thresh 0.3".format(img_path))