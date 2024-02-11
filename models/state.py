#!/usr/bin/python3
""" This module defines the state class
"""

from models.base_model import BaseModel

class State(BaseModel):
	""" State class definition
	"""
	def __init__(self, *args, **kwargs):
		self.name = ''
		super().__init__(*args, **kwargs)