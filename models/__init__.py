#!/usr/bin/python3
"""module create a unique FileStorage instance for
application
magic module which nitializes models package
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
