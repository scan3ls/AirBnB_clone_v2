#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String

class State(BaseModel, Base):
    """ State class """
    
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # change DBStorage so that when a state is deleted,
    #   delete all relevant cities of that state automagikly

    # ---  v WHATEVER THIS MEANS v --- #
    # for FileStorage: getter attribute cities that returns 
    #   the list of City instances with state_id equals to 
    #   the current State.id => It will be the FileStorage 
    #   relationship between State and City
    # ---  ^ WHATEVER THIS MEANS ^ --- #