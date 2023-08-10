#!/usr/bin/python3
"""
The module contains BaseModel template (class)
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    The base class for all classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization method
        """
        self.id = str(uuid.uuid4())
        kwargs.pop('__class__', None)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if (len(kwargs)):
            for key, value in kwargs.items():
                if (key not in ['created_at', 'updated_at']):
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = datetime.fromisoformat(value)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of an instance
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public attribute "updated_at"
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all the instance
        attributes and its class name
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return (instance_dict)

