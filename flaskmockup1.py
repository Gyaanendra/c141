from flask import Flask , jsonify , request
import pandas as pd 

all_movies = list(pd.read_csv("movies.csv"))
watched_movies = []


app = Flask(__name__)    

@app.route("/get-movies",methods=["GET"])

def  getmovie():
    return jsonify({
        "data":all_movies[0],
        "status":"message",
    })
    

@app.route("/watched-movies",methods=["POST"])

def watchmovies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    watched_movies.append(movies)
    return jsonify({
        "status":"message",
    }),201

if __name__ == "__main__":
    app.run(debug=True)
    
    