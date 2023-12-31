#!/usr/bin/python3
"""Class definition of a City"""

from sqlalchemy import Column, Integer, String, text, ForeignKey
from relationship_state import Base


class City(Base):
    """Class City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
