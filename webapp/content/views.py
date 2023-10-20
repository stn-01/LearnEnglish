from alphabet import ALPHABET
from syllables import SYLLABLES

from flask import Blueprint, render_template


blueprint = Blueprint('content', __name__, url_prefix='/content')


@blueprint.route('/alphabet')
def alphabet_page():
    alphabet_for_render_template = {f"{letter}_letter": ALPHABET[letter] for letter in 'abcdefghijklmnopqrstuvwxyz'}
    return render_template('alphabet.html', page_title='Алфавит',
                           **alphabet_for_render_template)


@blueprint.route('/syllables')
def syllables_page():
    syllables = ''
    return render_template('syllables.html', page_title='Слоги',
                           syllables=syllables)


@blueprint.route('/syllables/<letter>')
def letter_syllables_page(letter):
    syllables = SYLLABLES.get(letter)
    if not syllables:
        return render_template('index.html',
                               page_title=f'Слоги c {letter.upper()}')
    return render_template('syllables.html',
                           page_title=f'Слоги c {letter.upper()}',
                           syllables=syllables,
                           letter=letter)
