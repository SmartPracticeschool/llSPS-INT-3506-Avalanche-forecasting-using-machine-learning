# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:42:09 2020

@author: prem
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:34:00 2020

"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load

app = Flask(__name__)
model = load('Avalanche.save')

@app.route('/')
def home():
    return render_template('Avalance_Frontend.html')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    #x_test = [[int(x) for x in request.form.values()]]
    a= request.form['slope']
    
    b=request.form['density']
    if(b=='Low Density'):
        b=1
    if(b=='Highly Dense'):
        b=0
    if(b=='Medium Density'):
        b=2
    c=request.form['snowdensity']
    d=request.form['air']
    e=request.form['wind']
    total = [[a,int(b),c,d,e]]
    prediction = model.predict(total)
    
    print(total)
    #job column
    #print(x_test)
    sc=load('avstandard.save')
    prediction = model.predict(sc.transform(total))
    print(prediction)
    output=prediction[0]
    if(output==0):
        return render_template('Avalance_Frontend.html', prediction_text="Low Risk of Avalanche")
    if(output==1):
        return render_template('Avalance_Frontend.html', prediction_text="Moderate Risk of Avalanche")
    else:
        return render_template('Avalance_Frontend.html',prediction_text="High Risk of Avalanche")

if __name__ == "__main__":
    app.run(debug=True)