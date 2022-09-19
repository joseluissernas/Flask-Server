# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:40:58 2022

@author: josel
"""

from PIL import Image
import cv2
import numpy as np

def categorizar(pathfile, model_trained):
    img = Image.open(pathfile)
    img = np.array(img).astype(float)/255

    img = cv2.resize(img, (224,224))
    prediccion = model_trained.predict(img.reshape(-1, 224, 224, 3))
    return np.argmax(prediccion[0], axis=-1)






