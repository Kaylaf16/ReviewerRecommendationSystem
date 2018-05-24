from app import app
from flask import render_template
from flask import request, abort,jsonify, redirect,url_for
from articleClustering import clustering
import requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/v1/search',methods=['POST'])
def search():
    if request.method =='POST':
        title = request.form.get('title')
        topTerms = clustering(title)
        prediction = topTerms[len(topTerms)-1]
        topTerms = topTerms[:-1]
        allTerms = []
        counter = len(topTerms)/10
        start = 0
        index = 10

        for i in range(int(counter)):
            allTerms.append(topTerms[start:index])
            start= start+10
            index= index+10

        return render_template('results.html',topTerms=allTerms,prediction=prediction)
