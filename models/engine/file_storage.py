#!/usr/bin/python3
"""
The class FileStorage is a class that define the new dictionary of the class
"""
import json
from datetime import datetime
from models import base_model


class FileStorage:
    """
    All the instance used listed:
    all(self):
    new(self, obj):
    save(self):
    reload(self):
    """

    __file_path = './file.json'
    __objects = {}

    def all(self):
        """
        Function - all(self):
            return the object
            Object:
                nothing
            Return:
                object
        """
        return(FileStorage.__objects)

    def new(self, obj):
        """
        Function - new(self, obj):
            add new object to the dict
            Object:
                copy(str): the dictionary of the file
            Return:
                nothing
        """
        copy = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[copy] = obj

    def save(self):
        """
        Function - save(self):
            save the new dictionary
            Object:
                file(str): the name of wherethe file is
                dict3(dict): the new dictionary
            Return:
                nothing
        """
        file = FileStorage.__file_path
        dict3 = {}
        for copy, bm_obj in FileStorage.__objects.items():
            dict3[copy] = bm_obj.to_json()
        with open(file, 'w') as f:
            json.dump(dict3, f)

    def reload(self):
        """
        Function - reload(self):
            reload a new dictionary
            Object:
                file(str): the name of wherethe file is
                FileStorage.__objects(dict): the new dictionary
            Return:
                nothing
        """
        file = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(file, 'r') as fileopen:
                new_objs = json.load(fileopen)
        except:
            return