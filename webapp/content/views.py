from alphabet import ALPHABET
from random import choice
from syllables import SYLLABLES

from flask import (Blueprint, render_template, flash,
                   url_for, session, redirect)
from flask_login import current_user
from webapp.content.forms import WordsForm
from webapp.user.models import User

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


@blueprint.route('/words', methods=['GET', 'POST'])
def task_words():
    title = 'Переведи слово'
    user = User.query.get(current_user.id)
    words = {'dog': 'собака', 'cat': 'кошка', 'time': 'время', 'house': 'дом',
             'world': 'мир', 'father': 'отец', 'mother': 'мать',
             'year': 'год', 'big': 'большой', 'fire': 'огонь',
             'king': 'король', 'moon': 'луна', 'river': 'река',
             'lake': 'озеро', 'city': 'город', 'gold': 'золото',
             'game': 'игра', 'snow': 'снег', 'best': 'лучший', 'step': 'шаг',
             'love': 'любовь', 'map': 'карта', 'road': 'дорога',
             'rain': 'дождь', 'egg': 'яйцо', 'size': 'размер', 'ice': 'лёд',
             'price': 'цена', 'forest': 'лес', 'window': 'окно',
             'sky': 'небо', 'job': 'работа', 'hope': 'надежда'}
    form = WordsForm()
    random_word = ''
    if form.validate_on_submit():
        translation = form.translation.data
        if 'random_word' not in session:
            session['random_word'] = choice(list(words.keys()))
        random_word = session['random_word']
        if words[random_word] == translation:
            flash('Верно! Так держать! Теперь вот это:')
            return redirect(url_for('content.task_words'))
        else:
            flash('Упс! Ошибочка вышла!'
                  ' Подумай ещё! Пока вот тебе другое слово')
            return redirect(url_for('content.task_words'))
    if 'random_word' not in session:
        session['random_word'] = choice(list(words.keys()))
    random_word = session['random_word']
    if 'random_word' in session:
        random_word = choice(list(words.keys()))
        session['random_word'] = random_word
    else:
        random_word = session['random_word']
    form.translation.data = ''
    return render_template('task_words.html', form=form,
                           page_title=title, random_word=random_word,
                           user=user)
