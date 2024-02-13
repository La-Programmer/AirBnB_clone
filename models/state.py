#!/usr/bin/python3
""" This module defines the state class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """The State class"""
    def __init__(self, *args, **kwargs):
        """ The initialization method of the state class
        """
        self.name = ""
        super().__init__(*args, **kwargs)
