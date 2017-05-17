from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Person(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key= True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    job_type = Column(String)
    want_accomodation = Column(String)
    room_allocated = Column(String)


class Room(Base):
    __tablename__ = 'Rooms'
    id = Column(Integer, primary_key= True, autoincrement=True)
    room_name = Column(String)
    room_type = Column(String)
    occupants = Column(String)


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
