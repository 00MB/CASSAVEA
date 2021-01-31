from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('lander.html')

@app.route('/photo')
def photomenu():
    return render_template('photo.html')

@app.route('/output')
def output():
    return render_template('output.html', infected = "True", probabilities = {"Healthy": 10, "CMD": 20, "CGM": 40, "CBSD": 80, "CBB": 40})