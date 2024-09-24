#!/usr/bin/python3
"""location class"""

import models
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from models.basemodel import BaseModel, Base

class Location(BaseModel, Base):
    """Location"""
    if models.storage_t == 'db':
        __tablename__ = 'location'
        address = Column(String(1024), nullable=False)
    else:
        address = ""
