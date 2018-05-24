#!/usr/bin/env python3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import numpy as np
import string as str
import csv

def clusterMe(documents,title):
    topTerms = [];
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)
    true_k = 8
    Model = KMeans(n_clusters = true_k, init ='k-means++', max_iter=100, n_init=1)
    Model.fit(X)

    print("Top terms per cluster:")
    centroids = Model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()

    for i in range(true_k):
        print ("Cluster %d:" % i)

        for ind in centroids[i, :10]:
            topTerms.append(terms[ind])
            print( ' %s' % terms[ind])
        print('\n')

    print("\n")
    print("Prediction")

    Y = vectorizer.transform(title)
    prediction = Model.predict(Y)
    topTerms.append(prediction)
    print(prediction)
    return topTerms
def clustering(title):
    data = []
    with open('AuthorData.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row[1])

    return(clusterMe(data,[title])) #uncomment this to test the algorithm
