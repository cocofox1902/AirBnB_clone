#!/usr/bin/python3
"""
The __init__ file is to not go in another init file and reload storage
"""
from models.engine.file_storage import FileStorage
import models


storage = FileStorage()
storage.reload()
