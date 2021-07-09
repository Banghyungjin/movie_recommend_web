from flask import Flask , request , render_template
from datetime import date
import json
from sklearn.feature_extraction.text import TfidfVectorizer , CountVectorizer
import pandas as pd
import requests
from fetch import movie, movie_collection

app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def index():
    if request.method =="GET":
        year = date.today().year
        id_year = f'http://api.themoviedb.org/3/discover/movie?api_key=da396cb4a1c47c5b912fda20fd3a3336&primary_release_year={year}&sort_by=popularity.desc'
        top_year = movie_collection()
        top_year.results = []
        top_year.fetch(id_year)
        genres = json.loads(requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=da396cb4a1c47c5b912fda20fd3a3336&language=en-US").text)
        top_genre_collection = []
        for genre in genres['genres']:
            # print(genre['id'])
            genre_id = 'https://api.themoviedb.org/3/discover/movie?api_key=da396cb4a1c47c5b912fda20fd3a3336&with_genres={}&sort_by=popularity.desc'.format(genre["id"])
            top_genre = movie_collection()
            top_genre.results = []
            top_genre.fetch(genre_id)
            top_genre_id = [top_genre.results, genre["name"]]
            top_genre_collection.append(top_genre_id)
        return render_template("home.html",top_year=top_year.results  , year=year ,top_genre=top_genre_collection )
    
    elif request.method == "POST":
        return render_template("landing.html")



if __name__ == "__main__":
    app.run(port=5000 ,debug=True)