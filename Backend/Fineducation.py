
from flask import Flask, render_template,request 
import datetime
import pandas as pd

app = Flask(__name__)

@app.route('/index.html')
def Landing():
    return render_template('index.html')

@app.route('/test.html')
def Intro():
    return render_template('test.html')

@app.route('/dasprojekt.html')
def my_form():
    return render_template('dasprojekt.html')

@app.route('/finanztypen.html')
def Geschichte():
    return render_template('finanztypen.html')

app.run()







