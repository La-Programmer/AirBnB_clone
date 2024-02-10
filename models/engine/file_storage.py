#!/usr/bin/python3
""" A module responsible for json serialization, deserialization
    and file storage
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
        """
        Sets obj in __objects with key <class name>.<obj.id>
        """
        key = "{}.{}".format(obj.__class__.__name__.obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ Serializes the __objects dict to a json file
        """
        serialized = {}
        for key, obj in self.__objects.items():
            # Use the to_dict method to serialize each object
            serialized[key] = obj.to_dict()
        
        data = json.dumps(serialized)
        with open(self.__file_path, 'w') as file:
            file.write(data)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                content = file.read()
            self.__objects = json.loads(content)
