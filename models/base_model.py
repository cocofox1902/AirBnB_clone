#!/usr/bin/python3
"""
class BaseModel is a class that defines
all common attributes/methods for other classes
"""
import models
import uuid
from datetime import datetime


def convertTime(obj):
    """
    Function - convertTime(obj):
        convert in date format

        Object:
            obj(datetime): date time to convert

        Return:
            the date in a datetime format
    """

    if type(obj) in [datetime]:
        obj = obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strptime(obj, "%Y-%m-%dT%H:%M:%S.%f")


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
                if first == "created_at":
                    self.created_at = convertTime(kwargs["created_at"])
                if first == "updated_at":
                    self.updated_at = convertTime(kwargs["updated_at"])
                if first == '__class__':
                    continue
                else:
                    setattr(self, first, second)
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today().isoformat()
            self.updated_at = datetime.today().isoformat()
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
        self.__dict__.update({
            "created_at": convertTime(self.created_at),
            "updated_at": convertTime(self.updated_at),
        })
        return("[{:s}] ({:s}) {}".format(
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
        if type(self.created_at) in [str]:
            self.created_at = convertTime(self.created_at)
        if type(self.updated_at) in [str]:
            self.updated_at = convertTime(self.updated_at)
        self.created_at = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dictnew = (self.__dict__).copy()
        dictnew['__class__'] = self.__class__.__name__
        return dictnew
