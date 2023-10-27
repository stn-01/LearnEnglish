from getpass import getpass
import sys

from webapp import create_app
from webapp.user.models import db, User

app = create_app()
with app.app_context():
    user_name = input('Введите своё имя: ')
    email = input('Введите свою электронную почту: ')
    nickname = input('Введите никнейм: ')

    if User.query.filter(User.email == email).count():
        print('Пользователь с такой электронной почтой уже зарегистирован!')
        sys.exit(0)

    if User.query.filter(User.nickname == nickname).count():
        print('Пользователь с таким ником уже существует!')
        sys.exit(0)

    password_1 = getpass('Введите пароль: ')
    password_2 = getpass('Повторите пароль: ')

    if not password_1 == password_2:
        print('Вы ввели разные пароли!')
        sys.exit(0)

    new_admin = User(name=user_name, email=email,
                     nickname=nickname, role='admin')
    new_admin.set_password(password_1)

    db.session.add(new_admin)
    db.session.commit()
    print(f'Пользователь {user_name} с ником {nickname}'
          ' успешно зарегистрирован. '
          f'Роль - админ. id={new_admin.id}')
