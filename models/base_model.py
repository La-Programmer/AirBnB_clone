#!/usr/bin/python3

"""Module that defines a class named BaseModel"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class definition
    """

    def __init__(self, *args, **kwargs):
        """Method to initialize the class attributes"""
        from models import storage
        if (kwargs):
            for i in kwargs.keys():
                if (i != '__class__'):
                    if (i == 'created_at' or i == 'updated_at'):
                        setattr(self, i, datetime.fromisoformat(kwargs[i]))
                    else:
                        setattr(self, i, kwargs[i])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Method for serialization"""
        serialized = dict(self.__dict__)
        serialized['__class__'] = self.__class__.__name__
        serialized.update({
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        })
        return serialized

    def __str__(self):
        """Returns a visualization of the class objects"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
