from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
import numpy as np


def path_to_tensor(img):
    # loads RGB image as PIL.Image.Image type
    # if the image mode is not RGB, convert it
    if img.mode != "RGB":
        img = image.convert("RGB")

    # resize the input image
    target = (224, 224)
    img = img.resize(target)

    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = img_to_array(img)

    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)