from flask import Flask, request, jsonify
from Database import MongoP,MongoP1
import tensorflow as tf
import numpy as np
import pandas as pd

model = tf.keras.models.load_model('./DeviceModel.h5')

def retPred(received_array):
    received_array = [float(element) for element in received_array]
    received_array=np.array(received_array)
    MongoP1(received_array)
    received_array= np.reshape(received_array,(1,-1))
    response1 =  model.predict(received_array)
    response = np.array2string(response1)
    return response