#!/usr/bin/python3
""" mysql database module """

class DBStorage():
    """ database class """

    __enigne = None
    __session = None

    def __init__(self):
        """ constructor """
        from sqlalchemy import create_engine
        self.__engine = create_engine(
            '''mysql+mysqldb://HBNB_MYSQL_USER:HBNBMYSQL_PWD\
            @HBNB_MYSQL_HOST/HBNB_MYSQL_DB''',
            pool_pre_ping=True
        )

    # TODO: This
    # if HBNB_ENV == "test":
    #   drop all tables

    def all(self, cls=None):
        """ query the database for all objects of class cls """

        # TODO: This

        # if cls=None:
        #   query all objects

        # return dictionary
        # key: <class__name__>.<object-id>
        # value: <dict(object)>

    def new(self, obj):
        """ add current obj to database """
        # TODO: This
        pass

    def save(self):
        """ commit all changes to database """
        # TODO: This
        pass

    def delete(self, obj=None):
        """ delete obj from database """
        # TODO: This
        pass

    def reload(self):
        """ Brain work better later """
        # TODO: This
        
        # create all tables in the database (feature of SQLAlchemy) 
        # (WARNING: all classes who inherit from Base must be imported 
        # before calling Base.metadata.create_all(engine))
        
        # create the current database session (self.__session) from 
        # the engine (self.__engine) by using a sessionmaker - the 
        # option expire_on_commit must be set to False ; and 
        # scoped_session - to make sure your Session is thread-safe

        pass