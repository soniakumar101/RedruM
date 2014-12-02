from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker, scoped_session

ENGINE = None
Session = None

engine = create_engine("sqlite:///username.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

#Creating user class that inherits base whatever from SQLAlhemy
class User(Base):
    #setting up the sql syntax for sqlalchemy
    __tablename__ = "users"

    #setting column names (or attributes in python) with variables for primary key
    #and nullable
    id = Column(Integer, primary_key = True)
    name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)

def connect():

    global ENGINE
    global Session
    ENGINE = create_engine("sqlite:///username.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return session 


def create_tables():

    Base.metadata.create_all(engine)
    pass




def main():
    pass

if __name__ == "__main__":
    main()