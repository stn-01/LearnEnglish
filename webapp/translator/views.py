from translate import Translator
from flask import Blueprint, render_template, flash, redirect, url_for
from webapp.translator.forms import TranslatorForm


blueprint = Blueprint('translator', __name__, url_prefix='/translator')
translator = Translator(from_lang='en', to_lang='ru')


@blueprint.route('/translate', methods=['GET', 'POST'])
def translator_func():
    title = 'Переводчик'
    form = TranslatorForm()
    if form.text.data:
        if len(form.text.data) > 500:
            flash('Допускается не более 500 символов')
            return redirect(url_for('translator.translator_func'))
        translated_text = translator.translate(form.text.data)
        form.translation.data = translated_text
    return render_template('translator/translator.html', form=form,
                           page_title=title)
