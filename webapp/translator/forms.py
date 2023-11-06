from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TranslatorForm(FlaskForm):
    text = StringField('Введите текст для перевода',
                       validators=[DataRequired()])
    translation = StringField('Перевод', validators=[DataRequired()])
    submit = SubmitField('Перевести', render_kw={'class': 'btn btn-success'})
