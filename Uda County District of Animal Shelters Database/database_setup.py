#Uda County District of Animal Shelters

import sys
import os
import datetime, enum

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'
	name = Column(String(100), nullable=False)
	address = Column(String(250))
	city = Column(String(50))
	state = Column(String(25))
	zipCode = Column(Integer)
	website = Column(String(250))
	id = Column(Integer, primary_key = True)

class Puppy(Base):
	__tablename__ = 'puppy'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	gender = Column(String(6), nullable = False)
	dateOfBirth = Column(DateTime)
	picture = Column(String)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	weight = Column(Numeric(10))

engine = create_engine('sqlite:///shelter_puppy_db.db')

Base.metadata.create_all(engine)

