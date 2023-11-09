# LearnEnglish

LearnEnglish - это веб-приложения для изучения английского языка.

## Установка
Не забудьте создать виртуальное окружение для проекта!
#### Клонируйте репоизиторий следующими командами в консоли:
```
git clone https://github.com/stn-01/LearnEnglish.git
```
ВНИМАНИЕ! В приложении используется СУБД PostgreSQL.

#### Создайте файл config.py в папке webapp и пропишите в нем следующие строки:
```
from datetime import timedelta
import os


NAME_DB = 'Имя базы данных'
NAME = 'Имя пользователя'
PASSWORD = 'Пароль БД'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'URI базы данных с подстановкой вышепрописанных значений'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'Ваш секретный ключ'
SESSION_TYPE = 'filesystem'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'Почта для приложения (с нее пользователям будут отправлятся письма)'
MAIL_DEFAULT_SENDER = 'еще раз укажите почу'
MAIL_PASSWORD = 'пароль почты (может потребоваться удаленный пароль, смотрите в аккаунте Google в разделе "Безопасность")'

REMEMBER_COOKIE_DURATION = timedelta(days=7)
```

Приложение упаковано в docker-контейнер, поэтому если у вас установлен docker, выполните следующие шаги

#### Выполните команды:
```
docker compose build
docker compose up
```
Должно отобразиться что-то вроде этого:
![Запуск через докер](/readme_screen.jpg)

Теперь вы можете зайти в приложение по ссылке 172.18.0.2:5000

## Запуск без docker
Для того, чтобы установить приложение к себе на компьютер без docer выполните следующие действия:
#### Установите зависимости, выполнив команду:
```
pip install -r requirements.txt
```
#### Запустите приложение, выполнив в консоли:
Для Linux и MacOS:
```
export FLASK_APP=webapp && export FLASK_ENV=development && export FLASK_DEBUG=1 && flask run

```
Для Windows:
```
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

```