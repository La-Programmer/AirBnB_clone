#!/usr/bin/python3
"""This module defines the User class
"""

from models.base_model import BaseModel
from . import storage

class User(BaseModel):
	""" The User class
	"""
	def __init__(self, *args, **kwargs):
		self.email = ''
		self.password = ''
		self.first_name = ''
		self.last_name = ''
		super().__init__(**kwargs)
