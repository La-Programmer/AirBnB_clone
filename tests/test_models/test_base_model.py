#!/usr/bin/python3
"""python3 -c 'print(__import__("test_base_model.py").__doc__)'
"""


import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
	"""python3 -c 'print(__import__("test_base_model.py").TestBaseModel__doc__)'
	"""

	@classmethod
	def setUpClass(self):
		"""python3 -c 'print(__import__("test_base_model.py").setUpClass__doc__)'
		"""
		self.firstbase = BaseModel()
		self.secondbase = BaseModel()
		self.thirdbase = BaseModel()
	
	@classmethod
	def tearDownClass(self):
		"""python3 -c 'print(__import__("test_base_model.py").tearDownClass__doc__)'
		"""
		del self.firstbase, self.secondbase, self.thirdbase
	
	def testPrint(self):
		"""python3 -c 'print(__import__("test_base_model.py").print__doc__)'
		"""
		self.firstbase.name = "My first instance"
		self.firstbase.number = 98
		self.assertEqual("[BaseModel] ({}) {}".format(self.firstbase.id, self.firstbase.__dict__), str(self.firstbase))

	def testSave(self):
		"""python3 -c 'print(__import__("test_base_model.py").save__doc__)'
		"""
		self.secondbase.save()
		self.assertNotEqual(self.secondbase.created_at, self.secondbase.updated_at)

	def testToDict(self):
		"""python3 -c 'print(__import__("test_base_model.py").to_dict__doc__)'
		"""
		print(self.thirdbase)
		dictionary = self.thirdbase.to_dict()
		dictionary1 = self.thirdbase.__dict__
		dictionary1.update({'__class__': "BaseModel"})
		dictionary1.update({'created_at': self.thirdbase.created_at.isoformat(), 'updated_at': self.thirdbase.updated_at.isoformat()})
		self.assertEqual(dictionary, dictionary1)
