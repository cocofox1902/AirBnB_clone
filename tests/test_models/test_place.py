#!/usr/bin/python3
"""
Test: class BaseModel is a class that defines
all common attributes/methods for other classes
"""


import unittest
from models import place
from models.place import Place
import os


class TestPlace(unittest.TestCase):
    """
    Test All city class:
    """

    def test_doc(self):
        """
        Test documentation
        """
        module = len(place.__doc__)
        self.assertGreater(module, 0)

        module_class = len(Place.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Place.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Place.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Place.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Place.to_dict.__doc__)
        self.assertGreater(module_class, 0)

    def test_Name(self):
        """
        Test name
        """
        self.assertIn("name", Place.__dict__)
        self.assertIsInstance(Place.name, str)
        
    def test_Equal(self):
        """
        test correct name
        """
        my_Place = Place()
        my_Place.name = "Hello"
        self.assertEqual(my_Place.name, "Hello")