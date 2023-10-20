from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    user_name = StringField('Ваше имя:', validators=[DataRequired()],
                            render_kw={'class': 'form-control'})
    nickname = StringField('Ваш никнейм:', validators=[DataRequired()],
                           render_kw={'class': 'form-control'})
    email = StringField('Ваша электронная почта:',
                        validators=[DataRequired(), Email()],
                        render_kw={'class': 'form-control'})
    password = PasswordField('Введите пароль:',
                             validators=[DataRequired()],
                             render_kw={'class': 'form-control'})
    reapet_password = PasswordField('Повторите пароль:',
                                    validators=[DataRequired(),
                                                EqualTo('password')],
                                    render_kw={'class': 'form-control'})
    submit = SubmitField('Зарегистрироваться',
                         render_kw={'class': 'btn btn-success'})


class LoginForm(FlaskForm):
    nickname2 = StringField('Ваш никнейм:', validators=[DataRequired()],
                            render_kw={'class': 'form-control'})
    password2 = PasswordField('Введите свой пароль:', validators=[DataRequired()],
                              render_kw={'class': 'form-control'})
    submit2 = SubmitField('Войти', render_kw={'class': 'btn btn-success'})
    remember_me = BooleanField('Запомнить меня', default=True,
                               render_kw={"class": "form-check-input"})
