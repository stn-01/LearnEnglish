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
    repeat_password = PasswordField('Повторите пароль:',
                                    validators=[DataRequired(),
                                                EqualTo('password')],
                                    render_kw={'class': 'form-control'})
    submit = SubmitField('Зарегистрироваться',
                         render_kw={'class': 'btn btn-success'})


class LoginForm(FlaskForm):
    nickname2 = StringField('Ваш никнейм:', validators=[DataRequired()],
                            render_kw={'class': 'form-control'})
    password2 = PasswordField('Введите свой пароль:',
                              validators=[DataRequired()],
                              render_kw={'class': 'form-control'})
    submit2 = SubmitField('Войти', render_kw={'class': 'btn btn-success'})
    remember_me = BooleanField('Запомнить меня', default=True,
                               render_kw={"class": "form-check-input"})


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Введите почту, к которой привязан ваш аккаунт',
                        validators=[DataRequired(), Email()],
                        render_kw={'class': 'form-control'})
    submit = SubmitField('Сбросить пароль',
                         render_kw={'class': 'btn btn-success'})


class ResetPasswordForm(FlaskForm):
    password1 = PasswordField('Введите новый пароль:',
                              validators=[DataRequired()],
                              render_kw={'class': 'form-control'})
    password2 = PasswordField('Повторите пароль:', validators=[DataRequired()],
                              render_kw={'class': 'form-control'})
    submit = SubmitField('Применить новый пароль',
                         render_kw={'class': 'btn btn-success'})


class ChangeNameForm(FlaskForm):
    new_name = StringField('Ваше новое имя:', validators=[DataRequired()],
                           render_kw={'class': 'form-control'})
    submit = SubmitField('Сохранить',
                         render_kw={'class': 'btn btn-success'})


class ChangeEmailForm(FlaskForm):
    new_email = StringField('Введите почту, которую '
                            'вы хотите привязать к аккаунту',
                            validators=[DataRequired(), Email()],
                            render_kw={'class': 'form-control'})
    submit = SubmitField('Сохранить',
                         render_kw={'class': 'btn btn-success'})


class ChangeNicknameForm(FlaskForm):
    new_nickname = StringField('Введите новый никнейм, с которым '
                               'Вы будете входить в аккаунт:',
                               validators=[DataRequired()],
                               render_kw={'class': 'form-control'})
    submit = SubmitField('Сохранить',
                         render_kw={'class': 'btn btn-success'})
