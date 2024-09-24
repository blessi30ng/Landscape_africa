#!/usr/bin/python3
"""contains DBStorage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.basemodel import Base
import os
import models
from models.basemodel import BaseModel
from models.user import User
from models.booking import Booking
from models.service import Service
from models.review import Review
from models.payment import Payment
from models.location import Location

classes = {"User": User,
           "Booking": Booking,
           "Service": Service,
           "Review": Review,
           "Payment": Payment,
           "Location": Location}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Initializes dbStorage"""

        LAND_MYSQL_USER = os.getenv('LAND_MYSQL_USER')
        LAND_MYSQL_PWD = os.getenv('LAND_MYSQL_PWD')
        LAND_MYSQL_HOST = os.getenv('LAND_MYSQL_HOST', 'localhost')
        LAND_MYSQL_DB = os.getenv('LAND_MYSQL_DB')
        LAND_ENV = os.getenv('LAND_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                LAND_MYSQL_USER,
                LAND_MYSQL_PWD,
                LAND_MYSQL_HOST,
                LAND_MYSQL_DB),
            pool_pre_ping=True
        )

        if LAND_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self,cls=None):
        """query current database"""
        result_dict = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result_dict[key] = obj
        else:
             for class_type in classes:
                query_result = self.__session.query(class_type).all()
                for obj in query_result:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result_dict[key] = obj

        return result_dict

    def new(self, obj):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads database session"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.remove()
