from flask import Flask, render_template, request

Valid_Login = "a"
Valid_Pass = "1"

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == ValidLogin and password == ValidPass:
            return render_template('link.html')
    return render_template('login.html')

@app.route('/me', methods=['GET', 'POST'])
def me():
    return render_template('me.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)