#!/usr/bin/python3
"""This file contains the BaseModel class"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """BaseModel class that defines all common attributes/methods"""

    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel class"""

        # if keyword argument is provided initialize class with the specified
        # values
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    val = datetime.fromisoformat(val)
                elif key == 'updated_at':
                    val = datetime.fromisoformat(val)
                self.__setattr__(key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

            models.storage.new(self)

    def __str__(self):
        """String representation of BaseModel"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updating the updated_at attribute with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returning a dictionary containing all keys/values of __dict__"""

        formatted_dict = self.__dict__.copy()
        formatted_dict['created_at'] = formatted_dict['created_at'].isoformat()
        formatted_dict['updated_at'] = formatted_dict['updated_at'].isoformat()
        formatted_dict['__class__'] = self.__class__.__name__
        return formatted_dict

