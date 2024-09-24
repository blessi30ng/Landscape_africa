#!/usr/bin/python3

"""class user"""

import models
from models.basemodel import BaseModel
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from models.basemodel import BaseModel, Base
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represents user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False, unique=True)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        location = Column(String(1024), nullable=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        location = ""


    bookings = relationship("Booking", back_populates="user", cascade="all, delete")
    payments = relationship("Payment", back_populates="user", cascade="all, delete")
    reviews = relationship("Review", back_populates="user", cascade="all, delete")
    services = relationship("Service", back_populates="user", cascade="all, delete")
