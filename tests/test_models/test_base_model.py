#!/usr/bin/python3
""" Represents the unittests for BaseModel. """
import unittest
from models.base_model import BaseModel
from datetime import datetime, date, time
from models.engine.file_storage import FileStorage
import json


class TestBaseModel(unittest.TestCase):
    """Defines the tests on BaseModel."""

    def setUp(self):
        """ sets up a BaseModel instance"""
        self.base_test = BaseModel()

    def test_for_public_attr(self):
        """ Tests the id, created_at and updated at attributes """
        list_attr = ["id", "created_at", "updated_at"]
        for attr in list_attr:
            self.assertTrue(hasattr(self.base_test, attr))

    def test_id_with_uuid4(self):
        """ Tests whether Id is a string """
        self. assertIsInstance(self.base_test.id, str)

    def test_datetime(self):
        """ Tests the created_at and update_at are datetime instances """
        self.assertIsInstance(self.base_test.created_at, datetime)
        self.assertIsInstance(self.base_test.updated_at, datetime)

    def test_init_kwargs(self):
        """ Tests if BaseModel instance can be created with a dictionary """
        obj = BaseModel(**self.base_test.to_dict())

        for k, v in self.base_test.__dict__.items():
            self.assertEqual(v, obj.__dict__[k])

    def test_to_dict(self):
        """ checks if the dictionary key-value pairs are valid"""
        dict_obj = self.base_test.to_dict()
        self.assertIsInstance(datetime.fromisoformat(dict_obj['created_at']),
                              datetime)
        self.assertIsInstance(datetime.fromisoformat(dict_obj['updated_at']),
                              datetime)

        self.assertEqual(dict_obj['__class__'], 'BaseModel')

    def test_save(self):
        """ checks if save updates updated_at """
        date_obj = self.base_test.updated_at
        self.base_test.save()
        self.assertIsInstance(date_obj, datetime)

    def test_datetime_isoformat_in_to_dict(self):
        """checks if to_dict stores dates in isoformat"""
        dict_obj = self.base_test.to_dict()

        for k, v in self.base_test.__dict__.items():
            if isinstance(self.base_test.__dict__[k], datetime):
                self.assertEqual(datetime.fromisoformat(dict_obj[k]), v)


if __name__ == "__main__":
    unittest.main()
