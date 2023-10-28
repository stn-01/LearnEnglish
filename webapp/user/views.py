from flask import (Blueprint, render_template,
                   flash, url_for, redirect)
from flask_login import (current_user,
                         login_user, logout_user)
from webapp.user.models import db, User
from webapp.user.forms import (LoginForm, RegisterForm,
                               ResetPasswordRequestForm, ResetPasswordForm,
                               ChangeEmailForm, ChangeNameForm,
                               ChangeNicknameForm)
from webapp.email.send_email import (send_welcome_email,
                                     send_password_reset_email)

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


@blueprint.route('/profile/<nickname>')
def profile(nickname):
    page_title = 'Профиль'
    user = User.query.filter_by(nickname=nickname).first()
    return render_template('profile.html', user=user, page_title=page_title)


@blueprint.route('/reset-password-request', methods=['GET', 'POST'])
def reset_password_request():
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        if not User.query.filter(User.email == form.email.data).count():
            flash('Ошибка! Пользователь с такой электронной почтой'
                  ' не найден')
            return redirect(url_for('users.reset_password_request'))
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('На указанную почту отправлены'
              ' инструкции по восстановлению пароля')
        return redirect(url_for('users.login'))
    return render_template('reset_password.html',
                           title='Сброс пароля', form=form)


@blueprint.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('homepage'))
    reset_form = ResetPasswordForm()
    if reset_form.validate_on_submit():
        if reset_form.password1.data == reset_form.password2.data:
            new_password = reset_form.password1.data
            user.set_password(new_password)
            db.session.merge(user)
            db.session.commit()
            flash('Ваш пароль успешно изменен')
            return redirect(url_for('users.login'))
        else:
            flash('Пароли не совпадают!')
    return render_template('new_password.html',
                           title='Сброс пароля', reset_form=reset_form)


@blueprint.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    user = User.query.get(current_user.id)
    reset_form = ResetPasswordForm()
    if reset_form.validate_on_submit():
        if reset_form.password1.data == reset_form.password2.data:
            new_password = reset_form.password1.data
            user.set_password(new_password)
            db.session.merge(user)
            db.session.commit()
            flash('Ваш пароль успешно изменен')
            return redirect(url_for('users.profile', nickname=user.nickname))
        else:
            flash('Пароли не совпадают!')
    return render_template('new_password.html',
                           title='Изменение пароля', reset_form=reset_form)


@blueprint.route('/change_name', methods=['GET', 'POST'])
def change_name():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    user = User.query.get(current_user.id)
    name_form = ChangeNameForm()
    if name_form.validate_on_submit():
        new_name = name_form.new_name.data
        user.name = new_name
        db.session.merge(user)
        db.session.commit()
        flash('Ваше имя успешно изменено')
        return redirect(url_for('users.profile', nickname=user.nickname))
    return render_template('change_user_data.html',
                           title='Изменение имени пользователя',
                           name_form=name_form,
                           show_new_nickname=False,
                           show_new_name=True,
                           show_new_email=False)


@blueprint.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    user = User.query.get(current_user.id)
    email_form = ChangeEmailForm()
    if email_form.validate_on_submit():
        print(email_form.errors)
        new_email = email_form.new_email.data
        if User.query.filter(User.email == new_email).first():
            return flash('Ошибка! Пользователь с такой электронной почтой'
                         'уже зарегистрирован')
        user.email = new_email
        db.session.merge(user)
        db.session.commit()
        flash('Ваша почта успешно изменена')
        return redirect(url_for('users.profile', nickname=user.nickname))
    return render_template('change_user_data.html',
                           title='Изменение почты пользователя',
                           email_form=email_form,
                           show_new_nickname=False,
                           show_new_name=False,
                           show_new_email=True)


@blueprint.route('/change_nickname', methods=['GET', 'POST'])
def change_nickname():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    user = User.query.get(current_user.id)
    nickname_form = ChangeNicknameForm()
    if nickname_form.validate_on_submit():
        new_nickname = nickname_form.new_nickname.data
        if User.query.filter(User.nickname == new_nickname).first():
            return flash('Ошибка! Пользователь с таким ником уже'
                         'зарегистрирован')
        user.nickname = new_nickname
        db.session.merge(user)
        db.session.commit()
        flash('Ваш никнейм успешно изменен')
        return redirect(url_for('users.profile', nickname=user.nickname))
    return render_template('change_user_data.html',
                           title='Изменение никнейма пользователя',
                           nickname_form=nickname_form,
                           show_new_nickname=True,
                           show_new_name=False,
                           show_new_email=False)
