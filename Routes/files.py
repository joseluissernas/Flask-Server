# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:11:56 2022

@author: josel
"""

from flask import Blueprint, request, send_from_directory
from os import getcwd, path, remove
from responses.response_json import response_json
import tensorflow as tf
from predict import categorizar

routes_files = Blueprint("routes_files", __name__)

PATH_FILE = getcwd() + "/files/"

@routes_files.post("/upload")
def upload_file():  
    try:
        file = request.files['file']
        file.save(PATH_FILE + file.filename)
        return response_json("uploaded successfully" + PATH_FILE + file.filename)
    except FileNotFoundError:
        return response_json("Folder not found", 404)
    
@routes_files.get("/file/<string:name_file>")
def get_file(name_file):
    return send_from_directory(PATH_FILE, path=name_file, as_attachment=False)

@routes_files.get("/download/<string:name_file>")
def download_file(name_file):
    return send_from_directory(PATH_FILE, path=name_file, as_attachment=True)

@routes_files.delete("/delete")
def delete_file():
    filename = request.form['filename']
    
    if path.isfile(PATH_FILE + filename) == False:
        return response_json("file does not exist", 404)
    else:
        try:
            remove(PATH_FILE + filename)
            return response_json("file deleted")
        except OSError:
            return response_json(OSError, 404)
    
@routes_files.post("/predict")
def predict():
    try:
        file = request.files['file']
        file.save(PATH_FILE + file.filename)
        pathfile = (PATH_FILE + file.filename)
        model_trained = tf.keras.models.load_model("C:/Users/josel/OneDrive/Escritorio/Server_Flask/App/saved_model.h5")
        prediction = categorizar(pathfile,model_trained)
        return response_json(str(prediction))
    except FileNotFoundError:
        return response_json("Folder not found", 404)
    
    



    
    
    
    
      