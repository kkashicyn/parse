import re
from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html' )

@app.route("/data")    
def data():
    data = []

    for item in ['4lapy.json', 'lemur.json', 'petshop.json']:
        with open('data/'+item) as f:
            data+=json.load(f)
    
    query = ''
    if request.args.get('query') != None:
        query = request.args.get('query').lower()
    
    #if query and query != '':
    data_tmp = []
    for item in data:
        if query in item['title'].lower():
           data_tmp.append(item)
           
    data = data_tmp        

    return jsonify(data), 200
    