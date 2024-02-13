#!/usr/bin/python3
"""Module that defines a class named Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class"""
    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
