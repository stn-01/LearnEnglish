from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WordsForm(FlaskForm):
    translation = StringField('Введите перевод слова',
                              validators=[DataRequired()])
    submit = SubmitField('Проверить', render_kw={'class': 'btn btn-success'})
