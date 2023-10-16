#!/usr/bin/python3
"""Unittest module for the Review Class."""


import unittest
import os
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.review = Review()
        self.attributes = storage.attributes().get("Review", {})

    def tearDown(self):
        """Clean up the test environment after each test."""
        del self.review
        self.resetStorage()

    def resetStorage(self):
        """Reset the FileStorage data for a clean state."""
        storage.reload()

    def test_instantiation(self):
        """Test if an instance of Review can be created."""
        self.assertIsInstance(self.review, Review)
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attributes_existence(self):
        """Test if attributes exist in the Review instance."""
        for attr_name, attr_type in self.attributes.items():
            self.assertTrue(hasattr(self.review, attr_name))
            self.assertIsInstance(getattr(self.review, attr_name), attr_type)


if __name__ == "__main__":
    unittest.main()
