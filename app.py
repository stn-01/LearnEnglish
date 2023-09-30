from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', page_title='Главная')


@app.route('/alphabet')
def alphabet_page():
    return render_template('alphabet.html', page_title='Алфавит')


@app.route('/syllables')
def syllables_page():
    return render_template('syllables.html', page_title='Слоги')


if __name__ == '__main__':
    app.run(debug=True)
