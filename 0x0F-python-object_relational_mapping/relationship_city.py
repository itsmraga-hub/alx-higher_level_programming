#!/usr/bin/python3

"""
    Python file that contains the class definition
    of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
        A state class linking to table states
        __table_name__ - Table name
        id - primary key
        name - column name, string
        state_id - foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
