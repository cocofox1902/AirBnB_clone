#!/usr/bin/python3
"""
classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    public class atributes: state_id(str)
    public class atributes: name(str)
    """
    state_id = ''
    name = ''
