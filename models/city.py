#!/usr/bin/python3
""" This module defines the city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The City class"""
    def __init__(self, *args, **kwargs):
        """ The initialization method of the city class
        """
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
