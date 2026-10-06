from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "rating": 8.7,
        "genre": "комедия",
        "description": "ква"
    },
    {
        "id": 2,
        "title": "Матрица",
        "year": 1999,
        "rating": 8.5,
        "genre": "научная фантастика",
        "description": "мяу"
    },
    {
        "id": 3,
        "title": "Шрек",
        "year": 2001,
        "rating": 8.1,
        "genre": "хоррор",
        "description": "кар-кар"
    },
{
        "id": 4,
        "title": "Бесславные ублюдки",
        "year": 2009,
        "rating": 8.0,
        "genre": "боевик",
        "description": "мур"
    },
{
        "id": 5,
        "title": "Дурак",
        "year": 2014,
        "rating": 8.1,
        "genre": "драма",
        "description": "дом упал"
    }
]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie.html", movie=movie)

    return "Фильм не найден", 404


if __name__ == "__main__":
    app.run(debug=True)



