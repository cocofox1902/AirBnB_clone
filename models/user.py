#!/usr/bin/python3
"""
classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    public class atributes: email(str)
    public class atributes: password(str)
    public class atributes: first_name(str)
    public class atributes: last_name(str)
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
