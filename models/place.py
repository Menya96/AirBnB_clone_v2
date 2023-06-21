#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
from models import storage_type


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(
            String(60), ForeignKey('cities.id'), nullable=False
            ) if storage_type == 'db' else ""
    user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False
            ) if storage_type == 'db' else ""
    name = Column(
            String(128), nullable=False
            ) if storage_type == 'db' else ""
    description = Column(
            String(1024), nullable=True
            ) if storage_type == 'db' else ""
    number_rooms = Column(
            Integer, default=0, nullable=False
            ) if storage_type == 'db' else 0
    number_bathrooms = Column(
            Integer, default=0, nullable=False
            ) if storage_type == 'db' else 0
    max_guest = Column(
            Integer, default=0, nullable=False
            ) if storage_type == 'db' else 0
    price_by_night = Column(
            Integer, default=0, nullable=False
            ) if storage_type == 'db' else 0
    latitude = Column(
            Float
            ) if storage_type == 'db' else 0.0
    longitude = Column(
            Float
            ) if storage_type == 'db' else 0.0
    amenity_ids = []

    if storage_type == 'db':
        reviews = relationship(
                'Review',
                cascade='all, delete, delete-orphan',
                backref='place'
                )
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                viewonly=False,
                backref='place_amenities'
                )
    else:
        @property
        def reviews(self):
            """Returns the reviews of this Place"""
            from models import storage
            reviews_of_place = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_of_place.append(value)
            return reviews_of_place

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            from models import storage
            amenities_of_place = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_of_place.append(value)
            return amenities_of_place

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
