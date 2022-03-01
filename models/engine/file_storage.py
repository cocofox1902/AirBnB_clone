#!/usr/bin/python3
"""
"""
import json
from datetime import datetime
from models import base_model


class FileStorage:
    """
    """

    __file_path = './file.json'
    __objects = {}


    def all(self):
        """
        """
        return(FileStorage.__objects)

    def new(self, obj):
        """
        """
        copy = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[copy] = obj

    def save(self):
        """
        """
        file = FileStorage.__file_path
        dict3 = {}
        for copy, bm_obj in FileStorage.__objects.items():
            dict3[copy] = bm_obj.to_json()
        with open(file, 'w') as f:
            json.dump(dict3, f)

    def reload(self):
        """
        """
        file = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(file, 'r') as fileopen:
                new_objs = json.load(fileopen)
        except:
            return