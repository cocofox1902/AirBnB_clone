#!/usr/bin/python3
"""
Test: class BaseModel is a class that defines
all common attributes/methods for other classes
"""


import unittest
from models import state
from models.state import State
import os


class Teststate(unittest.TestCase):
    """
    Test All city class:
    """

    def test_doc(self):
        """
        Test documentation
        """
        module = len(state.__doc__)
        self.assertGreater(module, 0)

        module_class = len(State.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(State.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(State.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(State.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(State.to_dict.__doc__)
        self.assertGreater(module_class, 0)

    def test_Name(self):
        """
        Test name
        """
        self.assertIn("name", State.__dict__)
        self.assertIsInstance(State.name, str)
        
    def test_Equal(self):
        """
        test correct name
        """
        my_State = State()
        my_State.name = "Hello"
        self.assertEqual(my_State.name, "Hello")