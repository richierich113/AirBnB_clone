#!/usr/bin/python3
"""Unittest module for the City Class."""


import unittest
import os
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.city = City()
        self.attributes = storage.attributes().get("City", {})

    def tearDown(self):
        """Clean up the test environment after each test."""
        del self.city
        self.resetStorage()

    def resetStorage(self):
        """Reset the FileStorage data for a clean state."""
        storage.reload()

    def test_instantiation(self):
        """Test if an instance of City can be created."""
        self.assertIsInstance(self.city, City)
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attributes_existence(self):
        """Test if attributes exist in the City instance."""
        for attr_name, attr_type in self.attributes.items():
            self.assertTrue(hasattr(self.city, attr_name))
            self.assertIsInstance(getattr(self.city, attr_name), attr_type)


if __name__ == "__main__":
    unittest.main()
