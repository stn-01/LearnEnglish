from flask import Blueprint, render_template, flash, url_for, redirect
from flask_login import (current_user,
                         login_user, logout_user)
from webapp.user.models import db, User
from webapp.user.forms import LoginForm, RegisterForm
from webapp.email.send_email import send_welcome_email

blueprint = Blueprint('users', __name__, url_prefix='/users')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Добро пожаловать на Learn English'
    if current_user.is_authenticated:
        flash('Вы уже авторизированы')
        return redirect(url_for('homepage'))
    login_form = LoginForm()
    register_form = RegisterForm()
    if login_form.validate_on_submit():
        return redirect(url_for('users.login'))
    return render_template('login.html', page_title=title,
                           login_form=login_form,
                           register_form=register_form, show_register=False)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Добро пожаловать на Learn English'
    if current_user.is_authenticated:
        flash('Вы уже зарегистрированы!')
        return redirect(url_for('homepage'))
    login_form = LoginForm()
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user_name = register_form.user_name.data
        nickname = register_form.nickname.data
        email = register_form.email.data
        password = register_form.password.data
        new_user = User(name=user_name, nickname=nickname,
                        email=email, password=password, role='user')
        if User.query.filter(User.email == email).count():
            return flash('Ошибка! Пользователь с такой электронной почтой'
                         'уже зарегистрирован')
        elif User.query.filter(User.nickname == nickname).count():
            return flash('Ошибка! Пользователь с таким ником уже'
                         'зарегистрирован')
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались. Войдите в аккаунт!')
        return send_welcome_email(new_user.email)
    return render_template('login.html', page_title=title,
                           login_form=login_form,
                           register_form=register_form, show_register=True)


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно вышли из своего аккаунта')
    return redirect(url_for('homepage'))


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nickname=form.nickname2.data).first()
        if user and user.check_password(password=form.password2.data):
            login_user(user)
            flash('Вы успешно авторизировались')
            return redirect(url_for('homepage'))
    flash('Неправильный логин(никнейм) или пароль')
    return redirect(url_for('users.login'))
