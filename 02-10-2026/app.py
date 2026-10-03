from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "rating": 8.7,
        "genre": "Фантастика, драма",
        "description": "Группа исследователей отправляется через червоточину в космосе, чтобы найти новый дом для человечества."
    },
    {
        "id": 2,
        "title": "Матрица",
        "year": 1999,
        "rating": 8.5,
        "genre": "Фантастика, боевик",
        "description": "Нео узнаёт, что привычный мир является искусственной реальностью, и присоединяется к борьбе за свободу."
    },
    {
        "id": 3,
        "title": "Шрек",
        "year": 2001,
        "rating": 8.1,
        "genre": "Мультфильм, комедия, фэнтези",
        "description": "Одинокий огр отправляется в путешествие, которое неожиданно меняет его жизнь."
    },
    {
        "id": 4,
        "title": "Начало",
        "year": 2010,
        "rating": 8.8,
        "genre": "Фантастика, триллер",
        "description": "Профессионал проникает в сны людей и получает сложное задание внедрить идею в подсознание."
    },
    {
        "id": 5,
        "title": "Властелин колец: Братство Кольца",
        "year": 2001,
        "rating": 8.9,
        "genre": "Фэнтези, приключения",
        "description": "Хранитель Кольца и его спутники отправляются в опасное путешествие, чтобы уничтожить могущественный артефакт."
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
