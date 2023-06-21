#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class defines the DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """This method initializes the DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This method queries on the current database session"""
        from models.base_model import BaseModel
        from models.engine.file_storage import FileStorage

        classes = {"User": User, "State": State,
                   "City": City, "Amenity": Amenity,
                   "Place": Place, "Review": Review}
        if cls is None:
            objs = []
            for c in classes.values():
                objs += self.__session.query(c).all()
        else:
            if cls in classes:
                objs = self.__session.query(classes[cls]).all()
            else:
                objs = []
        return {obj.__class__.__name__ + '.' + obj.id: obj for obj in objs}

    def new(self, obj):
        """This method adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """This method commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """This method deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """This method creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''Closes the storage engine'''
        self.__session.remove()
