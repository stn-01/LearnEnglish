from sqlalchemy import Column, Integer, String
from db import Base, engine

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)
    email = Column(String(120), unique=True)


    def __repr__(self):
        return f'<User {self.name} {self.nickname} {self.email}>'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)