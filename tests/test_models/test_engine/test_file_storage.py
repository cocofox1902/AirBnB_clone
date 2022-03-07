#!/usr/bin/python3
"""
Test: class file_storage is a class that defines
all common attributes/methods for other classes
"""


import unittest
from datetime import datetime
from models import base_model
from models.base_model import BaseModel
import os
from time import sleep
import pycodestyle
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from models.engine import file_storage
import json
import sys


class TestFile_Storage(unittest.TestCase):
    """
    All the instance used listed:
        all(self):
        new(self, obj):
        save(self):
        reload(self):
    """

    def test_doc(self):
        """
        Test documentation
        """
        self.assertGreater(len(base_model.__doc__), 0)
        self.assertGreater(len(BaseModel.__doc__), 0)
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)
        self.assertGreater(len(BaseModel.save.__doc__), 0)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)

    def test_style(self):
        """
        Test style
        """
        style = pycodestyle.StyleGuide(quiet=True).check_files(["models/base_model.py"])
        self.assertEqual(style.total_errors, 0, "style errors")

    def test_save(self):
        BaseModel_test = BaseModel()
        Amenity_test = Amenity()
        Place_test = Place()
        City_test = City()
        Review_test = Review()
        State_test = State()
        User_test = User()
        models.storage.save()
        with open("file.json", 'r') as f:
            jsonfile = json.load(f)
        for AllClass in ["BaseModel." + BaseModel_test.id,
                          "Amenity." + Amenity_test.id,
                          "Place." + Place_test.id,
                          "City." + City_test.id,
                          "Review." + Review_test.id,
                          "State." + State_test.id,
                          "User." + User_test.id]:
            self.assertIn(AllClass, jsonfile.keys())

    def test_reload(self):
        BaseModel_test = BaseModel()
        Amenity_test = Amenity()
        Place_test = Place()
        City_test = City()
        Review_test = Review()
        State_test = State()
        User_test = User()
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        models.storage.reload()
        with open("file.json", 'r') as f:
            jsonfile = json.load(f)
        for AllClass in ["BaseModel." + BaseModel_test.id,
                          "Amenity." + Amenity_test.id,
                          "Place." + Place_test.id,
                          "City." + City_test.id,
                          "Review." + Review_test.id,
                          "State." + State_test.id,
                          "User." + User_test.id]:
            self.assertIn(AllClass, jsonfile.keys())

    def test_new(self):
        BaseModel_test = BaseModel()
        Amenity_test = Amenity()
        Place_test = Place()
        City_test = City()
        Review_test = Review()
        State_test = State()
        User_test = User()
        for AllClass in ["BaseModel." + BaseModel_test.id,
                          "Amenity." + Amenity_test.id,
                          "Place." + Place_test.id,
                          "City." + City_test.id,
                          "Review." + Review_test.id,
                          "State." + State_test.id,
                          "User." + User_test.id]:
            self.assertIn(AllClass, models.storage.all().keys())

    def test_attributes_assignement(self):
        self.assertIn("_FileStorage__objects", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIn("_FileStorage__file_path", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
