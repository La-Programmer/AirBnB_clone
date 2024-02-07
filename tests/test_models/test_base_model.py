#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test instances before each test"""
        self.first_base = BaseModel()
        self.second_base = BaseModel()
        self.third_base = BaseModel()

    def tearDown(self):
        """Clean up after each test"""
        del self.first_base, self.second_base, self.third_base

    def test_str_representation(self):
        """Test the string representation of BaseModel"""
        self.first_base.name = "My first instance"
        self.first_base.number = 98
        expected_str = "[BaseModel] ({}) {}".format(self.first_base.id, self.first_base.__dict__)
        self.assertEqual(expected_str, str(self.first_base))

    def test_save_method_updates_updated_at(self):
        """Test that the save method updates the updated_at attribute"""
        initial_updated_at = self.second_base.updated_at
        self.second_base.save()
        self.assertNotEqual(initial_updated_at, self.second_base.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        dictionary = self.third_base.to_dict()
        expected_dict = self.third_base.__dict__.copy()
        expected_dict['__class__'] = "BaseModel"
        expected_dict['created_at'] = self.third_base.created_at.isoformat()
        expected_dict['updated_at'] = self.third_base.updated_at.isoformat()
        self.assertEqual(dictionary, expected_dict)

    def test_recreating_instance_from_dict(self):
        """Test recreating an instance from its dictionary representation"""
        dict_representation = self.first_base.to_dict()
        new_instance = BaseModel(**dict_representation)
        self.assertEqual(str(self.first_base), str(new_instance))
        self.assertFalse(new_instance is self.first_base)

    def test_default_attributes(self):
        """Test the default attributes of BaseModel"""
        self.assertIsNotNone(self.first_base.id)
        self.assertIsNotNone(self.first_base.created_at)
        self.assertIsNotNone(self.first_base.updated_at)

    def test_attribute_types(self):
        """Test the types of attributes in BaseModel"""
        self.assertIsInstance(self.second_base.id, str)
        self.assertIsInstance(self.second_base.created_at, datetime)
        self.assertIsInstance(self.second_base.updated_at, datetime)

    def test_custom_attribute(self):
        """Test adding a custom attribute to BaseModel"""
        self.first_base.custom_attribute = "Custom Value"
        self.assertEqual("Custom Value", self.first_base.custom_attribute)

    def test_deserialization_with_empty_dict(self):
        """Test deserialization with an empty dictionary"""
        empty_dict_instance = BaseModel(**{})
        self.assertIsNotNone(empty_dict_instance.id)
        self.assertIsNotNone(empty_dict_instance.created_at)
        self.assertIsNotNone(empty_dict_instance.updated_at)

if __name__ == '__main__':
    unittest.main()
