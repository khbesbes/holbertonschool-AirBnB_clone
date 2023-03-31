#!/usr/bin/python3

"""
This module defines the FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode="w",
                  encoding="utf-8") as f:
            obj_dict = {key: obj.to_dict() for key,
                        obj in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path,
                      mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = key.split(".")[0]
                    if cls_name in self.classes:
                        cls = self.classes[cls_name]
                        obj = cls(**value)
                        self.new(obj)
        except FileNotFoundError:
            pass
