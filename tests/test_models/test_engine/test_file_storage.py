#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """ Sets up fileStorage instance, and reloads. """
        self.fileStorage = FileStorage()
        self.fileStorage.reload()

    def test_private_attributes(self):
        """ Tests the attributes for the FileStorage instance."""
        self.assertTrue(hasattr(self.fileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.fileStorage, "_FileStorage__objects"))

    def test_dict_methods(self):
        """ Tests the dictionary methods of the fileStorage class"""
        all_instances = self.fileStorage.all()
        self.assertIsInstance(all_instances, dict)
        self.assertEqual(all_instances, self.fileStorage._FileStorage__objects)

    def test_new(self):
        """Tests if obj.__class__.__name__}.{obj.id} key is added to obj dict"""
        obj = BaseModel()
        self.fileStorage.new(obj)
        key = (f"{obj.__class__.__name__}.{obj.id}")
        self.assertIn(key, self.fileStorage._FileStorage__objects)
        self.assertEqual(self.fileStorage._FileStorage__objects[key], obj)

    def test_save(self):
        """ Tests if the new FileStorage instance is saved """
        obj = BaseModel()
        self.fileStorage.new(obj)
        self.fileStorage.save()
        pathname = self.fileStorage._FileStorage__file_path
        with open(pathname, 'r') as f:
            new_dict = f.read()
            self.assertIn(obj.__class__.__name__, new_dict)
            self.assertIn(obj.id, new_dict)

    def test_reload(self):
        """ Tests if instances are loaded to object dictionary"""
        obj = BaseModel()
        self.fileStorage.new(obj)
        self.fileStorage.save()
        self.fileStorage.reload()
        key = (f"{obj.__class__.__name__}.{obj.id}")
        self.assertIn(key, self.fileStorage._FileStorage__objects)

    def tearDown(self):
        """ closes open file"""
        pathname = self.fileStorage._FileStorage__file_path
        try:
            os.remove(pathname)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
