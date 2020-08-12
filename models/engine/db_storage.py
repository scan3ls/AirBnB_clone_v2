#!/usr/bin/python3
"""A RANDOM DOCSTRING"""

class DBStorage()
    """CLASS DBSTORAGE"""
    __engine = None
    __session = None

    def __init__(self):
        """INIT"""
        from sqlalchemy import (create_engine)
        import os

        usr = os.enviorn.get("HBNB_MYSQL_USER")
        pwd = os.enviorn.get("HBNB_MYSQL_PWD")
        host = os.enviorn.get("HBNB_MYSQL_HOST")
        db = os.enviorn.get("HBNB_MYSQL_DB")
        env = os.enviorn.get("HBNB_ENV")

        up = "mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, host, db)
        self.__engine = create_engine(up, pool_pre_ping=True)

        self.__session = sessionmaker(bind = self.__engine)()
        # To Do: drop all tables if the environment variable HBNB_ENV is equal to test

    def all(self, cls=None):
        """all"""
        if cls is not None:
            cls_name = cls.__name__
            return self.__session.query(cls_name).all()
        # TO DO!

    def new(self, obj):
        """adds a new object to the session"""
        cls_name, id, key = obj.__name__, obj.id, cls_name + id
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
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User

        Base.metadata.create_all(self.__engine)
