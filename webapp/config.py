from datetime import timedelta
import os


NAME_DB = 'rzipkbfg'
NAME = 'rzipkbfg'
PASSWORD = 'NZbTiKQC3EZ0I3EZB0qzIBWY50w7GYC8'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'postgresql+psycopg2://{NAME}:{PASSWORD}@cornelius.db.elephantsql.com:5432/{NAME_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False


SECRET_KEY = 'vdv$gEFw!fker329fdslsdjkge#geww*vqwvsvl'
SESSION_TYPE = 'filesystem'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'learnenglish.lp.project@gmail.com'
MAIL_DEFAULT_SENDER = 'learnenglish.lp.project@gmail.com'
MAIL_PASSWORD = 'wsnj pogh kubv xeke'

REMEMBER_COOKIE_DURATION = timedelta(days=7)
