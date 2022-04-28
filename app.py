from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html' )

@app.route("/data")    
def data():

    reviews = []
    #, '4lapy.json' ,'lemur.json', 'petshop.json'
    for item in ['4lapy.json' ,'lemur.json', 'petshop.json']:
        with open('data/'+item) as f:
            reviews+=json.load(f)
    
    query = ''
    if request.args.get('query') != None:
        query = request.args.get('query').lower()
    
    #if query and query != '':
    reviews_tmp = []
    for item in reviews:
        if query in item['title'].lower():
           reviews_tmp.append(item)

    reviews = reviews_tmp        

    marks = []


    with open('data/marks.json') as f:
        marks+=json.load(f)
    
    query = ''
    if request.args.get('query') != None:
        query = request.args.get('query').lower()
    
    #if query and query != '':
    marks_tmp = []
    for item in marks:
        if query in item['title'].lower():
           marks_tmp.append(item)

    marks = marks_tmp     

    return jsonify({'reviews': reviews, 'marks': marks}), 200
    