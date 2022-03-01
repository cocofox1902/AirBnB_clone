#!/usr/bin/python3
"""
class BaseModel is a class that defines
all common attributes/methods for other classes
"""
import json
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    All the instance used listed:
    __init__(self, *args, **kwargs):
    __str__(self):
    save(self):
    to_dict(self):
    """

    def __init__(self, *args, **kwargs):
        """
        Function - __init__(self, *args, **kwargs):
            assigned the value to the instance
            Object:
                id(str): the id of the class
                created_at(*): the date when the class is used
                updated_at(*): the date when the class is updated
            Return:
                nothing
        """
        if kwargs is not None:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """
        Function - __str__(self):
            print the information of the class
            Object:
                nothing
            Return:
                the class name, the id, and the dictionairy
        """
        return("[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                ))

    def save(self):
        """
        Function - save(self):
            update the time when the class is used
            Object:
                updated_at(*): the date when the class is updated
            Return:
                nothing
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Function - to_dict(self):
            the ditionary of the class
            Object:
                dict_2(dict): the new dictionary of the class
            Return:
                the new dictionary
        """
        dict_2 = dict(self.__dict__)
        dict_2['__class__'] = self.__class__.__name__
        dict_2['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_2['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return(dict_2)
