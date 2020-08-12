#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table

class Amenity(BaseModel, Base):
    name = ""

    __tablename__ = "amenities"
    name = Column(String(128),
                  nullable=False)
    association_table = Table('association',
                              Base.metadata,
                              Column('left'
                                     Integer,
                                     ForeignKey('left.id')),
                              Column('right')
    place_amenities = 
