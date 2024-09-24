#!/usr/bin/python3

"""payment class"""

import models
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from models.basemodel import BaseModel, Base
from datetime import datetime

class Payment(BaseModel, Base):
    """payments"""
    if models.storage_t == 'db':
        __tablename__ = 'payments'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        amount = Column(Float, nullable=False)
        payment_date = Column(DateTime, default=datetime.utcnow)
        payment_status = Column(String(20), nullable=False)
    else:
        user_id = ""
        amount = 0.0 #Amount paid
        payment_date = ""
        payment_status = ""
