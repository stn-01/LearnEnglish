from config import NAME, NAME_DB, PASSWORD
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(
    f'postgresql://{NAME}:{PASSWORD}@cornelius.db.elephantsql.com/{NAME_DB}'
    )
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

