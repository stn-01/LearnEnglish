import os

from flask_admin import Admin
from flask import Flask, render_template, flash, url_for, redirect
from flask_login import (LoginManager, current_user,
                         login_user, logout_user)
from flask_materialize import Material
from flask_mail import Mail, Message
from webapp.admin_panel import DashboardView, UserView
from webapp.models import db, User
from webapp.forms import LoginForm, RegisterForm
from webapp.config import MAIL_DEFAULT_SENDER


def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(),
                'webapp/templates'))
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    admin = Admin(app, index_view=DashboardView(),
                  endpoint='admin')
    material = Material(app)
    admin.add_view(UserView(User, db.session, name='Пользователи'))

    mail = Mail(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def homepage():
        return render_template('index.html', page_title='Главная')

    @app.route('/alphabet')
    def alphabet_page():
        return render_template('alphabet.html', page_title='Алфавит')

    @app.route('/syllables')
    def syllables_page():
        return render_template('syllables.html', page_title='Слоги')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        title = 'Регистрация и авторизация'
        if current_user.is_authenticated:
            flash('Вы уже авторизированы')
            return redirect(url_for('homepage'))
        login_form = LoginForm()
        register_form = RegisterForm()
        if login_form.validate_on_submit():
            return redirect(url_for('login'))
        return render_template('login.html', page_title=title,
                               login_form=login_form,
                               register_form=register_form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        title = 'Регистрация и авторизация'
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
            return send_welcome_email_test(new_user.email)
        return render_template('login.html', page_title=title,
                               login_form=login_form,
                               register_form=register_form)

    @app.route('/send-first-msg')
    def send_welcome_email_test(email_to):
        user = User.query.filter_by(email=email_to).first()
        if not user:
            return redirect(url_for('login'))
        msg = Message(sender=MAIL_DEFAULT_SENDER,
                      recipients=[email_to])
        welcome_email = render_template('email/welcome.html', user=user)
        msg.html = welcome_email
        mail.send(msg)
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно вышли из своего аккаунта')
        return redirect(url_for('homepage'))

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(nickname=form.nickname2.data).first()
            if user and user.check_password(password=form.password2.data):
                login_user(user)
                flash('Вы успешно авторизировались')
                return redirect(url_for('homepage'))
        flash('Неправильный логин(никнейм) или пароль')
        return redirect(url_for('login'))

    return app
