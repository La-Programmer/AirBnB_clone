#!/usr/bin/python3
""" This module defines the city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The City class"""
    state_id = ""
    name = ""
