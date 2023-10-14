#!/usr/bin/python3
"""module create a unique FileStorage instance for
application
magic module which nitializes models package
"""


from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
