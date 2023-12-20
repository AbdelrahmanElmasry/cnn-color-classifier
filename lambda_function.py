#!/usr/bin/env python
# coding: utf-8
import numpy as np
import tflite_runtime.interpreter as tflite
from PIL import Image
import requests

classes = ['black',
 'blue',
 'brown',
 'green',
 'grey',
 'orange',
 'pink',
 'purple',
 'red',
 'silver',
 'white',
 'yellow'
]

def load_img(image_path, target_size = 150):
    if(image_path.startswith('http://') or image_path.startswith('https://')):
        img = Image.open(requests.get(image_path, stream=True).raw)
    else:
        img = Image.open(image_path)
    img = img.resize((target_size, target_size), Image.NEAREST)
    return img

def preprocess_input(x):
    x /= 127.5
    x -= 1.
    return x

def prepare_img_input(img_path):
    img = load_img(img_path, target_size = 299)
    x = np.array(img, dtype='float32')
    X = np.array([x])

    X = preprocess_input(X)

    return X

interpreter = tflite.Interpreter(model_path='color-classifier-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


def predict(url):
    interpreter.set_tensor(input_index, prepare_img_input(url))
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)

    decimal_preds = preds[0].tolist()

    return dict(zip(classes, decimal_preds))

def lambda_handler(event, context):
    url = event['url']
    return predict(url)

