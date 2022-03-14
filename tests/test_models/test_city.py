#!/usr/bin/python3
"""
Test: class BaseModel is a class that defines
all common attributes/methods for other classes
"""


import unittest
from models import city
from models.city import City
import os


class TestCity(unittest.TestCase):
    """
    Test All city class:
    """

    def test_doc(self):
        """
        Test documentation
        """
        module = len(city.__doc__)
        self.assertGreater(module, 0)

        module_class = len(City.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(City.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(City.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(City.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(City.to_dict.__doc__)
        self.assertGreater(module_class, 0)

    def test_Name(self):
        """
        Test name
        """
        self.assertIn("name", City.__dict__)
        self.assertIsInstance(City.name, str)
        
    def test_Equal(self):
        """
        test correct name
        """
        my_City = City()
        my_City.name = "Hello"
        self.assertEqual(my_City.name, "Hello")