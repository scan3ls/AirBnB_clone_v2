#!/usr/bin/python3
"""A RANDOM DOCSTRING"""


class DBStorage():
    """CLASS DBSTORAGE"""
    __engine = None
    __session = None

    def __init__(self):
        """INIT"""
        from sqlalchemy import (create_engine)
        import os

        usr = os.environ.get("HBNB_MYSQL_USER")
        pwd = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        db = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")

        up = "mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, host, db)
        self.__engine = create_engine(up, pool_pre_ping=True)

        # To Do: drop all tables if  HBNB_ENV is equal to test

    def all(self, cls=None):
        """all"""

        return_dict = {}

        if cls is not None:
            result = self.__session.query(cls).all()
            for item in result:
                key = "{}.{}".format(item.to_dict()['__class__'], item.id)
                value = item
                return_dict.update({key: value})
                # print(return_dict)
            return return_dict
        # TO DO!

    def new(self, obj):
        """adds a new object to the session"""
        cls_name, id = obj.__class__.__name__, obj.id
        key = "{}.{}".format(cls_name, id)
        self.__session.add(obj)

    def save(self):
        """Actually commits the changes made to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all the databases"""
        from models.base_model import BaseModel, Base
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User
        from sqlalchemy.orm import sessionmaker

        Base.metadata.create_all(self.__engine)

        self.__session = sessionmaker(bind=self.__engine)()

    def close(self):
        """ close the session """
        self.__session.close()
