#!/usr/bin/python3
"""Unittest module for the Amenity Class."""


import unittest
import os
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.amenity = Amenity()
        self.attributes = storage.attributes().get("Amenity", {})

    def tearDown(self):
        """Clean up the test environment after each test."""
        del self.amenity
        self.resetStorage()

    def resetStorage(self):
        """Reset the FileStorage data for a clean state."""
        storage.reload()

    def test_instantiation(self):
        """Test if an instance of Amenity can be created."""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attributes_existence(self):
        """Test if attributes exist in the Amenity instance."""
        for attr_name, attr_type in self.attributes.items():
            self.assertTrue(hasattr(self.amenity, attr_name))
            self.assertIsInstance(getattr(self.amenity, attr_name), attr_type)

if __name__ == "__main__":
    unittest.main()
