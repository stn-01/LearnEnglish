import db
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/alphabet')
def alphabet_page():
    return render_template('alphabet.html')


@app.route('/syllables')
def syllables_page():
    return render_template('syllables.html')


if __name__ == '__main__':
    app.run(debug=True)
