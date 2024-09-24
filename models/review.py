#!/usr/bin/python3

"""Class review"""
import models
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from models.basemodel import BaseModel, Base

class Review(BaseModel, Base):
    """represents review"""
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        user_id = ""
        text = ""
