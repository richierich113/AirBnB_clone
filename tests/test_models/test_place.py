#!/usr/bin/python3
"""Unittest module for the Place Class."""


import unittest
import os
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.place = Place()
        self.attributes = storage.attributes().get("Place", {})

    def tearDown(self):
        """Clean up the test environment after each test."""
        del self.place
        self.resetStorage()

    def resetStorage(self):
        """Reset the FileStorage data for a clean state."""
        storage.reload()

    def test_instantiation(self):
        """Test if an instance of Place can be created."""
        self.assertIsInstance(self.place, Place)
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_attributes_existence(self):
        """Test if attributes exist in the Place instance."""
        for attr_name, attr_type in self.attributes.items():
            self.assertTrue(hasattr(self.place, attr_name))
            self.assertIsInstance(getattr(self.place, attr_name), attr_type)

if __name__ == "__main__":
    unittest.main()
