#!/usr/bin/python3
""" A module responsible for json serialization, deserialization and file storage
"""

import os
import json

class FileStorage():
	""" A class to handle file storage
	"""
	def __init__(self):
		""" Constructor function
		"""
		self.__file_path = "file.json"
		self.__objects = {}

	def all(self):
		""" Returns a dictionary that stores all objects
		"""
		return self.__objects

	def new(self, obj):
		""" Sets an obj in __objects with key <class name>.id
		"""
		self.__objects.update({f'{obj.__class__.__name__}.{obj.id}': obj.to_dict()})

	def save(self):
		""" Serializes the __objects dict to a json file
		"""
		data = json.dumps(self.__objects)
		with open(self.__file_path, 'w') as file:
			file.write(data)

	def reload(self):
		""" Deserializes the JSON file to __objects
		"""
		if os.path.exists(self.__file_path):
			with open(self.__file_path, 'r') as file:
				content = file.read()
			self.__objects = json.loads(content)
