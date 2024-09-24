#!/usr/bin/python3
"""Basemoedel class"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import uuid4
import json
import models

Base = declarative_base()

class BaseModel:
    """Basemodel class"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwarg) -> None:
        """Initializes basemodel"""
        if kwarg:
            for k, v in kwarg.items():
                if k == "__class__":
                    continue
                if k in ["created_at", "updated_at"] and isinstance(v, str):
                    v = datetime.fromisoformat(v)
                    pass

                setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at


    def __str__(self):
        """representation of string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """converts to dictionary"""
        to_json = self.__dict__
        to_json["class"] = self.__class__.__name__
        if isinstance(to_json["created_at"], datetime):
            to_json["created_at"] = to_json["created_at"].isoformat()
        if "updated_at" in to_json and isinstance(to_json["updated_at"], datetime):
            to_json["updated_at"] = to_json["updated_at"].isoformat()

        if "_sa_instance_state" in to_json:
            del to_json["_sa_instance_state"]

        return to_json

    def delete(self):
        """Deletes instance from storage"""
        models.storage.delete(self)
