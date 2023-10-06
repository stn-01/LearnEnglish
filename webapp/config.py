import os


NAME_DB = 'rzipkbfg'
NAME = 'rzipkbfg'
PASSWORD = 'NZbTiKQC3EZ0I3EZB0qzIBWY50w7GYC8'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'postgresql+psycopg2://{NAME}:{PASSWORD}@cornelius.db.elephantsql.com:5432/{NAME_DB}'

SECRET_KEY = 'vdv$gEFw!fker329fdslsdjkge#geww*vqwvsvl'