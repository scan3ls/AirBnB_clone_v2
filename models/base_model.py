#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey


Base = declarative_base()


class BaseModel():
    """A base class for all hbnb models"""
    id = Column(String(60),
                primary_key=True,
                nullable=False)
    created_at = Column(String(128),
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(String(128),
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs.items()) <= 0:
            storage.new(self)
            return

        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key == "created_at" or key == "updated_at":
                value = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        from models import env_type

        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})

        if env_type == "db":
            dictionary['created_at'] = self.created_at  # .isoformat()
            dictionary['updated_at'] = self.updated_at  # .isoformat()
        else:
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
        try:
            dictionary.pop('_sa_instance_state')
        except:
            pass
        return dictionary

    def delete(self):
        """Deletes the instance from models.storage"""
        from models import storage
        storage.delete(self)
