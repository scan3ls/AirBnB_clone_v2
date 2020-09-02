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
    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete"
        )

    @property
    def cities(self):
        """Getter for the attribute, cities"""

        from models.__init__ import env_type
        # To Do - Fix the getter attr if needed for task 6"
        if env_type == "fs":
            from models.engine.file_storage import FileStorage

            objects = FileStorage.all(City)
            cities = []

            for keys, value in objects.items():
                if 'City' in keys and value.state_id == self.id:
                    cities.append(value)

            return cities
        else:
            return
