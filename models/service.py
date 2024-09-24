#!/usr/bin/python3
"""services class"""

import models
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from models.basemodel import BaseModel, Base

class Service(BaseModel, Base):
    """repreentse services"""
    if models.storage_t == 'db':
        __tablename__ = 'services'
        name = Column(String(128), nullable=False)
    else:
        name = ""
