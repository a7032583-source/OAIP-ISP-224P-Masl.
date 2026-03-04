from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    multi_num = 0
    text = "Введите число"

    if request.method == "POST":
            num = float(request.form["number"])
            multi_num = num * 2
            text = f"Ваше число {num}, умноженное на 2: {multi_num}"

    return render_template('index.html',
                           number=multi_num,
                           text=text,
                           title='Home page')
@app.route("/index2", methods=["GET", "POST"])
def index2():
    multi_num = 0
    text = "Введите число"
    pi = 3.14

    if request.method == "POST":
            r = float(request.form["r"])
            x = pi * r**2
            text = f"Площадь круга с радиусом {r} равна {x} "

    return render_template('index2.html',
                           number=multi_num,
                           text=text,
                           title='Home page')


if __name__ == "__main__":
    app.run(debug=True)