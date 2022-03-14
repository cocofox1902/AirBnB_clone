#!/usr/bin/python3
"""
Test: class BaseModel is a class that defines
all common attributes/methods for other classes
"""


import unittest
from models import user
from models.user import User
import os


class TestUser(unittest.TestCase):
    """
    Test All city class:
    """

    def test_doc(self):
        """
        Test documentation
        """
        module = len(user.__doc__)
        self.assertGreater(module, 0)

        module_class = len(User.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(User.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(User.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(User.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(User.to_dict.__doc__)
        self.assertGreater(module_class, 0)

    def test_Name(self):
        """
        Test name
        """
        self.assertIn("name", User.__dict__)
        self.assertIsInstance(User.name, str)
        
    def test_Equal(self):
        """
        test correct name
        """
        my_User = User()
        my_User.name = "Hello"
        self.assertEqual(my_User.name, "Hello")