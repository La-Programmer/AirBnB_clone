#!/usr/bin/python3
"""This module defines the User class
"""

from models.base_model import BaseModel
from . import storage


class User(BaseModel):
    """ The User class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
