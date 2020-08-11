#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
<<<<<<< HEAD
        # If all() doesn't get an input
        if cls == None:
            return FileStorage.__objects

        # If all() does get a class as input
        cls_name = cls.__name__
        index_of_objects = FileStorage.__objects.keys() # Gets an index of keys
                                                        # in the object

        # Take advantage of the index and scan for the class name
        filtered_dict = {}
        for objects in index_of_objects:
            if cls_name in objects:
                filtered_dict[objects] = FileStorage.__objects[objects]
        return filtered_dict
=======
        return FileStorage.__objects
>>>>>>> parent of 94906c0... Logan (#4)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes abject if required"""
<<<<<<< HEAD
        # Generate the object name
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in FileStorage.__objects:
            FileStorage.__objects.pop(key)
=======
        if obj in FileStorage.__objects:
            del FileStorage.__objects[obj]
>>>>>>> parent of 94906c0... Logan (#4)
