#!/usr/bin/python3
"""Module that defines a class named 'User' that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""