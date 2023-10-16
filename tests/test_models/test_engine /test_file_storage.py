#!/usr/bin/python3
"""Unittest module for the FileStorage class."""


import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """This method is called before each test method."""

    def setUp(self):
        # Reset the FileStorage data and remove the JSON file.
        self.reset_storage()

    def tearDown(self):
        """Reset the FileStorage data and remove the JSON file."""
        self.reset_storage()

    def reset_storage(self):
        """ Helper method to reset the FileStorage data.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Ensure that the storage object is an instance of FileStorage.
        """
        self.assertIsInstance(storage, FileStorage)

    def test_attributes(self):
        """Test class attributes.
        """
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})


if __name__ == '__main__':
    unittest.main()
