#!/usr/bin/python3
"""booking class"""

import models
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from models.basemodel import BaseModel, Base
from datetime import datetime

class Booking(BaseModel):

    if models.storage_t == "db":
        __tablename__ = 'bookings'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        date = Column(DateTime, default=datetime.utcnow)
        time = Column(String(60), nullable=False)
        location = Column(String(1024), nullable=False)
        status = Column(String(20), nullable=False)
        payment_status = Column(String(20), nullable=False)
        amount_paid = Column(Float, nullable=False)
    else:
        user_id = ""
        date = ""
        time = ""
        location = ""
        status = ""
        payment_status = ""
        amount_paid = 0.0
