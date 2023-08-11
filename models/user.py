#!/usr/bin/python3
"""This module defines a class User"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    __table_args__ = (
        {'mysql_default_charset': 'latin1'})

    email = Column(
            String(128), nullable=False
            ) if storage_type == 'db' else ''
    password = Column(
            String(128), nullable=False
            ) if storage_type == 'db' else ''
    first_name = Column(String(128)) if storage_type == 'db' else ''
    last_name = Column(String(128)) if storage_type == 'db' else ''

    places = relationship(
            'Place',
            cascade='all, delete, delete-orphan',
            backref='user'
            ) if storage_type == 'db' else None
    reviews = relationship(
            'Review',
            cascade='all, delete, delete-orphan',
            backref='user'
            ) if storage_type == 'db' else None
