# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
# Load the Random Forest CLassifier model
filename = 'weights/xg_boost_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)
    

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        b=[]
        b.append(float(request.form['avg-T']))
        b.append(float(request.form['max-T']))
        b.append(float(request.form['min-T']))
        b.append(float(request.form['slp']))
        b.append(float(request.form['h']))
        b.append(float(request.form['vv']))
        b.append(float(request.form['v']))
        b.append(float(request.form['vm']))
    
        a = ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM']
        b = pd.DataFrame(b)
        b = b.transpose()
        for i in range(0,8):
        		b = b.rename(columns={i : a[i]})
    
        my_prediction = int(loaded_model.predict(b))
        #my_prediction = int(my_prediction)[1:-1] 

        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)
