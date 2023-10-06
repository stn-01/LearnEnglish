from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.create_db import Base, engine


db = SQLAlchemy()

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String(25), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password = Column(String)
    role = Column(String(15), index=True)


    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password) 

    def __repr__(self):
        return f'<User {self.name} {self.nickname} {self.email} {self.role}>'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)