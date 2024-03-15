#!/usr/bin/python3
"""Defines the State class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base  # Import Base from relationship_city.py

class State(Base):
    """State class with SQLAlchemy"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    def __repr__(self):
        return "<State(id='%s', name='%s')>" % (self.id, self.name)

