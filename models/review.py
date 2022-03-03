#!/usr/bin/python3
"""
classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    public class atributes: place_id(str)
    public class atributes: user_id(str)
    public class atributes: text(str)
    """
    place_id = ''
    user_id = ''
    text = ''
