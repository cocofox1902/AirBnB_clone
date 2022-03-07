#!/usr/bin/python3
"""
Test: amenity
"""


import unittest
from models import amenity
from models.amenity import Amenity
import os


class TestAnemity(unittest.TestCase):
    """
    Test All from amenity
    """

    def test_doc(self):
        """
        Test documentation
        """
        module = len(amenity.__doc__)
        self.assertGreater(module, 0)

        module_class = len(Amenity.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Amenity.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Amenity.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Amenity.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Amenity.to_dict.__doc__)
        self.assertGreater(module_class, 0)

    def test_Name(self):
        """
        Test name
        """
        self.assertIn("name", Amenity.__dict__)
        self.assertIsInstance(Amenity.name, str)
        
    def test_Equal(self):
        """
        test correct name
        """
        my_Amenity = Amenity()
        my_Amenity.name = "Hello"
        self.assertEqual(my_Amenity.name, "Hello")

