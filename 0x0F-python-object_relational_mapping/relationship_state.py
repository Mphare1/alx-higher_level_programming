#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(
        Integer,
        unique=True,
        nullable=False,
        autoincrement=True,
        primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
