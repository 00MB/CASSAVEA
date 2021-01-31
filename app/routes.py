import os
from flask import Flask, flash, request, redirect, url_for, render_template
from app import app
import cv2 as cv
import numpy as np
from keras.models import model_from_json

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/')
@app.route('/index')
def index():
    return render_template('lander.html')

@app.route('/photo')
def photomenu():
    return render_template('photo.html')

@app.route('/output', methods = ['POST'])
def output():
    print(request)
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        print('No selected file')
        return redirect(request.url)
    if file:
        print('Saving {} as cassavea', file.filename)
        #filename = secure_filename(file.filename)
        file.save('cassavea.'+file.filename.split(".")[-1])
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")
        print("Loaded model from disk")

        filepath='cassavea.'+file.filename.split(".")[-1]
        img=cv.imread(filepath)
        img=cv.resize(img,(350,350))
        img.shape
        img=np.array([img])
        #print(img.shape)
        resultant_prediction=loaded_model.predict(img)
        resultant_prediction = list(map(lambda x: round((x * 100),2), resultant_prediction[0]))
        infected = "True"
        if max(resultant_prediction) == resultant_prediction[4]:
            infected = "False"
        # Call the model and return the output to output.html here

    return render_template('output.html', infected = infected, probabilities = resultant_prediction)