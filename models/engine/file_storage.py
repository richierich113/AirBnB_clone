#!/usr/bin/python3
"""This module uses the FileStorage class to
serializes instances to a JSON file and deserializes JSON file
to instances
"""


import os
import json
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity


class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file
    to instances
    """
    current_directory = os.getcwd()
    __file_path = os.path.join(current_directory, "file.json")
    __objects = dict()

    all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        if not hasattr(obj, 'to_dict'):
            raise TypeError("Object has no 'to_dict()' method.")

        obj_dict = obj.to_dict()
        key = f"{obj_dict['__class__']}.{obj_dict['id']}"
        self.__objects[key] = obj

    save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as myfile:
            dt = {key: v.to_dict() for key, v in self.__objects.items()}
            json.dump(dt, myfile)


    def classes(self):
        """returns a dictionary of  class name
        and their respective classses
        """
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    reload(self):
        """deserializes the JSON file to __objects only if the JSON file
        exists ; otherwise, does nothing.
        If the file doesn’t exist, no exception is raised
        """
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, 'r', encoding='utf-8') as myFile:
            try:
                obj_dict = json.load(myFile)
                self.__objects = {
                    key: self.classes()[v['__class__']](**v)
                    for key, v in obj_dict.items()
                }
            except json.JSONDecodeError:
                pass
