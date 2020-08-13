#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    # ---------------------------------- #
    #           DBStorage                #
    # ---------------------------------- #
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          default=0,
                          nullable=False)
    number_bathrooms = Column(Integer,
                              default=0,
                              nullable=False)
    max_guest = Column(Integer,
                       default=0,
                       nullable=False)
    price_by_night = Column(Integer,
                            default=0,
                            nullable=False)
    longitude = Column(Float,
                       nullable=True)
    latitude = Column(Float,
                      nullable=True)
    reviews = relationship("Review",
                backref="place",
                cascade="all, delete"
            )
    amenities = relationship('Amenity',
                              secondary='place_amenity',
                              backref="places",
                              viewonly=False)
    metadata = Base.metadata
    place_amenity = Table('place_amenity',
                           metadata,
                           Column('place_id',
                                   String(60),
                                   ForeignKey('places.id'),
                                   primary_key=True,
                                   nullable=False),
                            Column('amenity_id',
                                    String(60),
                                    ForeignKey('amenities.id'),
                                    primary_key=True,
                                    nullable=False))

        # ---------------------------------- #
        #           FileStorage              #
        # ---------------------------------- #
        # from models import storage
        # from models.amenity import Amenity
# 
        # city_id = ""
        # user_id = ""
        # name = ""
        # description = ""
        # number_rooms = 0
        # number_bathrooms = 0
        # max_guest = 0
        # price_by_night = 0
        # latitude = 0.0
        # longitude = 0.0
        # amenity_ids = []
        # amenities = []

    @property
    def amenities(self):
        """Getter method for the attr 'amenities'"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """Setter method for the attr 'amenities'"""
        if obj is not None and obj.__class__ == Amenity:
            self.amenity_ids.append(obj.id)
