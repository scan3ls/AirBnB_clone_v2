#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey

class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

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
    reviews = relationship("Review", back_populates="places", cascade="all, delete")
    # Last bullet point @ number 9
