from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    a = 0
    b = 0
    c = 0

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])

    return render_template('index.html',
                           a = a,
                           b = b,
                           c = c,
                           title='Home page')
@app.route("/<float:num1>/<operation>/<float:num2>/")
def index2(num1=0, operation='+', num2=0):
    return render_template('index2.html',
                           num1=num1,
                           num2=num2,
                           operation=operation,
                           title='Home page')
if __name__ == "__main__":
    app.run(debug=True)