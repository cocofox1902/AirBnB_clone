#!/usr/bin/python3
"""
Test: class BaseModel is a class that defines
all common attributes/methods for other classes
"""


import unittest
from models import review
from models.review import Review
import os


class TestRseview(unittest.TestCase):
    """
    Test All city class:
    """

    def test_doc(self):
        """
        Test documentation
        """
        module = len(review.__doc__)
        self.assertGreater(module, 0)

        module_class = len(Review.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Review.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Review.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Review.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Review.to_dict.__doc__)
        self.assertGreater(module_class, 0)

    def test_Name(self):
        """
        Test name
        """
        self.assertIn("name", Review.__dict__)
        self.assertIsInstance(Review.name, str)
        
    def test_Equal(self):
        """
        test correct name
        """
        my_Review = Review()
        my_Review.name = "Hello"
        self.assertEqual(my_Review.name, "Hello")