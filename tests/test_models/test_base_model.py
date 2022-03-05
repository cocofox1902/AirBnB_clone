#!/usr/bin/python3
"""
Test: class BaseModel is a class that defines
all common attributes/methods for other classes
"""


import unittest
from datetime import datetime
from models import base_model
from models.base_model import BaseModel
import os

class TestBaseModel(unittest.TestCase):
    """
    Test All the instance used listed:
        __init__(self, *args, **kwargs):
        __str__(self):
        save(self):
        to_dict(self):
    """

    def doc(self):
        """
        Test documentation
        """
        self.assertGreater(len(base_model.__doc__), 0)
        self.assertGreater(len(BaseModel.__doc__), 0)
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)
        self.assertGreater(len(BaseModel.save.__doc__), 0)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)
