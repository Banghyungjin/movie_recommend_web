from flask import Flask, request, render_template
from datetime import date
import json
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd

import requests
from fetch import movie, movie_collection

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    year = date.today().year
    id_year = f'http://api.themoviedb.org/3/discover/movie?api_key=da396cb4a1c47c5b912fda20fd3a3336&primary_release_year={year}&sort_by=popularity.desc'

    top_year = movie_collection()
    top_year.fetch(id_year)
    
    return top_year.results


if __name__=="__main__":
    app.run(port=5000, debug=True)