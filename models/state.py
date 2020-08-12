#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from models.city import City

class State(BaseModel, Base):
    """ State class """
    name = ""

    __tablename__ = "states"
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City", back_populates="states", cascade="all, delete")

    @property
    def cities(self):
        """Getter for the attribute, cities"""
        # To Do - Fix the getter attr if needed for task 6"
        return self.cities
