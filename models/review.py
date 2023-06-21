#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    place_id = Column(
            String(60), ForeignKey('places.id'), nullable=False
            ) if storage_type == 'db' else ""
    user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False
            ) if storage_type == 'db' else ""
    text = Column(
            String(1024), nullable=False
            ) if storage_type == 'db' else ""
