#!/usr/bin/python3
"""Module that defines the class named Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity class"""
    def __init__(self, *args, **kwargs):
        """ The initialization method of the amenity class
        """
        self.name = ""
        super().__init__(*args, **kwargs)
