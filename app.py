from flask import Flask, request, render_template
from datetime import date
import json
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd

import requests
from fetch import movie

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    year = date.today().year
    id_year = f'http://api.themoviedb.org/3/discover/movie?api_key=da396cb4a1c47c5b912fda20fd3a3336&primary_release_year={year}&sort_by=popularity.desc'
    results = json.loads(requests.get(id_year).text)["results"]
    for i in results:
            if i["id"] and i["title"] and i["poster_path"] and i["vote_average"] and i["release_date"] and i["overview"] and i["backdrop_path"]:
                results.append(movie(i["id"],i["title"],i["poster_path"],i["vote_average"],i["release_date"],i["overview"],i["backdrop_path"]))
    return results


if __name__=="__main__":
    app.run(port=5000, debug=True)