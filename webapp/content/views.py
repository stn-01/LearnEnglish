import time
from alphabet import ALPHABET
from random import choice
from syllables import SYLLABLES

from flask import (Blueprint, render_template, flash, redirect,
                   url_for, request)
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
             'world': 'мир', 'father': 'папа', 'mother': 'мама',
             'year': 'год', 'big': 'большой', 'fire': 'огонь',
             'king': 'король', 'moon': 'луна', 'river': 'река',
             'lake': 'озеро', 'city': 'город', 'gold': 'золото',
             'game': 'игра', 'snow': 'снег', 'best': 'лучший', 'step': 'шаг',
             'love': 'любовь', 'map': 'карта', 'road': 'дорога',
             'rain': 'дождь', 'egg': 'яйцо', 'size': 'размер', 'ice': 'лёд',
             'price': 'цена', 'forest': 'лес', 'window': 'окно',
             'sky': 'небо', 'job': 'работа', 'hope': 'надежда'}
    form = WordsForm()
    random_word = choice(list(words.keys()))
    print(random_word)
    if form.validate_on_submit():
        print('good')
        translation = form.translation.data
        if translation and translation == words[random_word]:
            flash('Верно! Так держать! Теперь вот это:')
            time.sleep(5)
            print('flash good')
            return redirect(url_for('content.task_words'), code=303,
                            method=request.method)
        else:
            flash('Упс! Ошибочка вышла! Подумай ещё!'
                  'Пока вот тебе другое слово')
            time.sleep(5)
            print('flash no')
            return redirect(url_for('content.task_words'), code=303,
                            method=request.method)
    form.translation.data = ''
    return render_template('task_words.html', form=form, page_title=title,
                           random_word=random_word, user=user)
