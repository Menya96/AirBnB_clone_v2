#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models import storage_type


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    state_id = Column(
            String(60), ForeignKey('states.id'), nullable=False
            ) if storage_type == 'db' else ''
    name = Column(
            String(128), nullable=False
            ) if storage_type == 'db' else ''
    places = relationship(
            'Place',
            cascade='all, delete, delete-orphan',
            backref='cities'
            ) if storage_type == 'db' else None
