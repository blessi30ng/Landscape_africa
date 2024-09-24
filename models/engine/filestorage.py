#!/usr/bin/python3

"""representatiion of filestorage"""
import json
import models
from models.basemodel import BaseModel, Base
from models.user import User
from models.booking import Booking
from models.service import Service
from models.review import Review
from models.payment import Payment
from models.location import Location

class FileStorage:
    """filestorage class"""
    
    CLASSES = {"BaseModel": BaseModel, 
               "User": User, 
               "Booking": Booking, 
                "Service": Service, 
                "Review": Review,
                "Payment": Payment, 
                "Location": Location}

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """all"""
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
            return filtered_objects

    def new(self, obj):
        """new"""
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.__objects[key] = obj

    def save(self):
        """save"""
        serialized_obj = {}

        for k, v in self.__objects.items():
            serialized_obj[k] = v.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_obj, file, indent=2)

    def reload(self):
        """reloads """
        try:
            with open(self.__file_path, "r") as file:
                content = json.load(file)

                for k, v in content.items():
                    class_name = v["__class__"]

                    if class_name in self.CLASSES:
                        instance = self.CLASSES[class_name](**v)

                        print("reloading instance", instance)
                        self.__objects[k] = instance
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error: Corrupted file. Could not load data.")

    def delete(self, obj=None):
        """Deletes obj from objects if it exists"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
