import db
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def return_hello():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
