#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    '''class Amenity'''

    __tablename__ = 'amenities'

    name = Column(
            String(128), nullable=False
            ) if storage_type == 'db' else ''
