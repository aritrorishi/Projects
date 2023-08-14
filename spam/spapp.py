import numpy as np
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('spamrun.pkl', 'rb')) 

# Create application
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('spamcheck.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    data1 = request.form['a']
    data2 = pd.Series(data1)
    prediction = model.predict(data2)
    
    output = prediction[0]
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('spamcheck.html', 
                               result = 'mail is spam')
    else:
        return render_template('spamcheck.html', 
                               result = 'mail is ham')

if __name__ == '__main__':
#Run the application
    app.run()  