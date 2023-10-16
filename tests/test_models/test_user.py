#!/usr/bin/python3
"""Unittest module for the User Class."""


import unittest
import os
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.user = User()
        self.attributes = storage.attributes().get("User", {})

    def tearDown(self):
        """Clean up the test environment after each test."""
        del self.user
        self.resetStorage()

    def resetStorage(self):
        """Reset the FileStorage data for a clean state."""
        storage.reload()

    def test_instantiation(self):
        """Test if an instance of User can be created."""
        self.assertIsInstance(self.user, User)
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attributes_existence(self):
        """Test if attributes exist in the User instance."""
        for attr_name, attr_type in self.attributes.items():
            self.assertTrue(hasattr(self.user, attr_name))
            self.assertIsInstance(getattr(self.user, attr_name), attr_type)


if __name__ == "__main__":
    unittest.main()
