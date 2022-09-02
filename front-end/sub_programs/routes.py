from sub_programs import app
from flask import request, render_template
import requests


@app.route('/', methods = ['GET'])
def home():
    time_stamp = requests.get('http://time-api:5000/time_stamp')
    response = requests.post('http://back-end:5000/back-end', json = {"ts": time_stamp.text})

    return render_template('index.html', output=response.text)

