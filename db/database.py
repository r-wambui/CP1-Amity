from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String)
    job_type = Column(String)


class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_name = Column(String)
    room_type = Column(String)


if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(bind=engine)
