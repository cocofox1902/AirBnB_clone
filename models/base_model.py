#!/usr/bin/python3
"""
class BaseModel is a class that defines
all common attributes/methods for other classes
"""


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
                args(*): the arguments
                kwargs(**): ths keyword of the arguments

            Return:
                nothing
        """
        if kwargs:
            for first, second in kwargs.items():
                if first != '__class__':
                    if first != 'created_at' and first != 'updated_at':
                        setattr(self, first, second)
                    else:
                        setattr(self, first, datetime.fromisoformat(second))
        else:
            time = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = time
            self.updated_at = time
            models.storage.new(self)

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
                nothing

            Return:
                nothing
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Function - to_dict(self):
            the ditionary of the class

            Object:
                nothing

            Return:
                the new dictionary
        """
        dict_new = self.__dict__.copy()
        dict_new["__class__"] = self.__class__.__name__
        dict_new["created_at"] = dict_new["created_at"].isoformat()
        dict_new["updated_at"] = dict_new["updated_at"].isoformat()
        return dict_new
