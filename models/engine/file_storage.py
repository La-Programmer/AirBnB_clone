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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ Serializes the __objects dict to a json file
        """
        data = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as file:
            file.write(data)

    def get_my_classes(self):
        """Returns a dictionary of supported classes"""
        my_classes = ['BaseModel', 'User', 'State']
        return my_classes

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = file.read()

            # Deserialize JSON to self.__objects
            self.__objects = json.loads(data)
