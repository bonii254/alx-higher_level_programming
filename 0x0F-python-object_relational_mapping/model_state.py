#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class representing a state
    Attributes:
        id (int): An auto-generated, unique integer representing the
        primary key.
        name (str): A string with a maximum of 128 characters representing
        the state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
