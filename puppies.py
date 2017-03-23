from sqlalchemy import Column, ForeignKey, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(80), nullable=False)
    address = Column(String(80), nullable=False)
    city = Column(String(40), nullable=False)
    state = Column(String(40), nullable=False)
    zipCode = Column(Integer, nullable=False)
    website = Column(String(80))
    id = Column(Integer, primary_key=True)


class Puppy(Base):
    __tablename__ = 'puppy'

    name = Column(String(80), nullable=False)
    dateOfBirth = Column(Date)
    gender = Column(String(20), nullable=False)
    weight = Column(Integer)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    picture = Column(String(80))
    id = Column(Integer, primary_key=True)


engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)
