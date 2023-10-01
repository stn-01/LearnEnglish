import os

from flask import Flask, render_template, flash, url_for, redirect
from flask_login import LoginManager, login_user, logout_user

from webapp.models import db, User
from webapp.forms import LoginForm, RegisterForm


def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route('/')
    def return_hello():
        return 'hello'


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        title = 'Регистрация и авторизация'
        login_form = LoginForm()
        register_form = RegisterForm()
        if login_form.validate_on_submit():
             return redirect(url_for('login'))
        return render_template('login.html', page_title=title, login_form=login_form, 
                               register_form=register_form)
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        title = 'Регистрация и авторизация'
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
                return flash('Ошибка! Пользователь с такой электронной почтой уже зарегистрирован')
            elif User.query.filter(User.nickname == nickname).count():
                return flash('Ошибка! Пользователь с таким ником уже зарегистрирован')
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()
            flash('Вы успешно зарегистрировались. Войдите в аккаунт!')
            return redirect(url_for('login'))
        return render_template('login.html', page_title=title, login_form=login_form, 
                               register_form=register_form)
    
    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно вышли из своего аккаунта')
        return redirect(url_for('login')) # 'login' заменить, когда будет готов шаблон главной страницы
    
    # выяснить, почему не проходит авторизация 
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(nickname=form.nickname2.data).first()
            if user and user.check_password(password=form.password2.data):
                login_user(user)
                flash('Вы успешно авторизировались')
                return redirect(url_for('login')) # 'login' заменить, когда будет готов шаблон главной страницы
        flash('Неправильный логин(никнейм) или пароль')
        return redirect(url_for('login'))


    return app

