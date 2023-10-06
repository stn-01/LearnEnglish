import db
from flask import Flask, render_template
from alphabet import ALPHABET
from syllables import SYLLABLES
app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def homepage():
    return render_template('index.html', page_title='Главная')


@app.route('/alphabet')
def alphabet_page():
    alphabet_for_render_template = {f"{letter}_letter": ALPHABET[letter] for letter in 'abcdefghijklmnopqrstuvwxyz'}
    return render_template('alphabet.html', page_title='Алфавит', **alphabet_for_render_template)


@app.route('/syllables')
def syllables_page():
    syllables = ''
    return render_template('syllables.html', page_title='Слоги', syllables=syllables)


@app.route('/syllables/<letter>')
def letter_syllables_page(letter):
    syllables = SYLLABLES.get(letter)
    if not syllables:
        return render_template('index.html', page_title=f'Слоги c {letter.upper()}')
    return render_template('syllables.html', page_title=f'Слоги c {letter.upper()}', syllables=syllables, letter=letter)


if __name__ == '__main__':
    app.run(debug=True)
