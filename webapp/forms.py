from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    user_name = StringField('Ваше имя:', validators=[DataRequired()],
                             render_kw={'class': 'form-control'})
    nickname = StringField('Ваш никнейм:', validators=[DataRequired()],
                           render_kw={'class': 'form-control'})
    email = StringField('Ваша электронная почта:', validators=[DataRequired()],
                        render_kw={'class': 'form-control'})
    password = PasswordField('Придумайте надежный пароль:', validators=[DataRequired()],
                             render_kw={'class': 'form-control'})
    submit = SubmitField('Зарегистрироваться', render_kw={'class': 'btn btn-success'})
   

class LoginForm(FlaskForm):
    nickname2 = StringField('Ваш никнейм:', validators=[DataRequired()],
                           render_kw={'class': 'form-control'})
    password2 = PasswordField('Введите свой пароль:', validators=[DataRequired()],
                             render_kw={'class': 'form-control'})
    submit2 = SubmitField('Войти', render_kw={'class': 'btn btn-success'})

