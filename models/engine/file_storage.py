#!/usr/bin/python3
""" A module responsible for json serialization, deserialization
    and file storage
"""

import os
import json
from models.user import User
from models.base_model import BaseModel


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
                # Read the entire file and save to the variable, content
                content = file.read()
            # Check if the file content is empty
            if content:
                # Convert/load JSON file back to python obj (dict)
                serialized = json.loads(content)

                # Iterate through the serialized dict
                for key, value in serialized.items():
                    # Extract class name and object ID
                    class_name, obj_id = key.split('.')

                    # Check for the class name
                    if class_name == 'BaseModel':
                        # Create instance of the calss
                        obj_instance = BaseModel(**value)
                    elif class_name == 'User':
                        obj_instance = User(**value)
                    else:
                        # Skip unknown classes
                        continue

                    # Set the object in __objects
                    self.__objects[key] = obj_instance

