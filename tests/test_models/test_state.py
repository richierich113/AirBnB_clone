#!/usr/bin/python3
"""Unittest module for the State Class."""


import unittest
import os
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.state = State()
        self.attributes = storage.attributes().get("State", {})

    def tearDown(self):
        """Clean up the test environment after each test."""
        del self.state
        self.resetStorage()

    def resetStorage(self):
        """Reset the FileStorage data for a clean state."""
        storage.reload()

    def test_instantiation(self):
        """Test if an instance of State can be created."""
        self.assertIsInstance(self.state, State)
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attributes_existence(self):
        """Test if attributes exist in the State instance."""
        for attr_name, attr_type in self.attributes.items():
            self.assertTrue(hasattr(self.state, attr_name))
            self.assertIsInstance(getattr(self.state, attr_name), attr_type)


if __name__ == "__main__":
    unittest.main()
