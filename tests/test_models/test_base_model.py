#!/usr/bin/python3
""" Represents the unittests for BaseModel. """
import unittests
from models.base_model import BaseModel
from datetime import datetime, date, time


class TestBaseModel(unittest.TestCase):
    """Defines the tests on BaseModel."""

    def setUp(self):
        """ sets up a BaseModel instance"""
        self.base_test = BaseModel()

    def test_for_public_attr(self):
        """ Tests the id, created_at and updated at attributes """
        list_attr = ["id", "created_at", "updated_at"]
        for attr in list_attr:
            self.assertTrue(hasattr(self.test_obj, attrib))`
