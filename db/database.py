from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Person(Base):
    __tablename__ = 'People'
    first_name = Column(String, primary_key=True)
    last_name = Column(String)
    job_type = Column(String)
    want_accomodation = Column(String)


class Room(Base):
    __tablename__ = 'Rooms'
    room_name = Column(String, primary_key=True)
    room_type = Column(String)


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
