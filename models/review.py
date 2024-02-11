#!/usr/bin/python3
"""Module that defines a class named Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class"""
    place_id = ""
    user_id = ""
    text = ""
