import psycopg2
from webapp.config import NAME, NAME_DB, PASSWORD
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

db_string = f'postgresql+psycopg2://{NAME}:{PASSWORD}@cornelius.db.elephantsql.com:5432/{NAME_DB}'
engine = create_engine(db_string)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

