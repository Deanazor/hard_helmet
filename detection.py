import os
from vortex.runtime.helper import InferenceHelper
# import vortex.runtime as vrt
# from vortex.development.utils.runtime_wrapper import RuntimeWrapper
import cv2
import numpy as np

# construct runtime model with visualization
kwargs = dict(
    model_path="model/helmet_model.onnx",
    runtime='cpu',
)
rt = InferenceHelper.create_runtime_model(**kwargs)
size = (480,640)

def Predict(img_path):
    os.system("cd darknet && ./darknet detector test data/obj.data cfg/yolov4-custom.cfg \
              ../weights/yolov4-custom_best.weights .{} -thresh 0.3 -dont_show -map".format(img_path))

def detr_predict(file):
    # prepare test image, as NHWC with BGR channel order
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    # img = np.flip(img,-1)
    # img = cv2.resize(img[0],size[::-1])[None,...]
    img = cv2.resize(img, size[::-1], interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, 0)
    print(img.shape)

    # prepare arguments for inference,
    # note that the name 'score_threshold'
    # will be forwarded to the actual runtime model
    # hence the name should match the actual model itself.
    kwargs = dict(
        score_threshold=0.3,
        visualize=True,
    )
    result = rt(img,**kwargs)
    # print(result['prediction'])
    visual = result['visualization'][0]
    visual = np.flip(visual,2)
    cv2.imwrite("static/predictions.jpg", visual)
    # return visual

    # if 'visualization' in result:
    #     # visualize first batch
    #     visual = result['visualization'][0]
    #     visual = np.flip(visual,2)
    #     plt.imshow(visual)
    #     plt.show()