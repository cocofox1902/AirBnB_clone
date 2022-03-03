#!/usr/bin/python3
"""
classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    public class atributes: city_id(str)
    public class atributes: user_id(str)
    public class atributes: name(str)
    public class atributes: description(int)
    public class atributes: number_bathrooms(int)
    public class atributes: max_guest(int)
    public class atributes: price_by_night(int)
    public class atributes: latitude(float)
    public class atributes: longitude(float)
    public class atributes: amenity(list of string)
    """
    city_id = ''
    user_id = ''
    name = ''
    description = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ['', '']
