#!/usr/bin/python3
"""Module for TestHBNBCommand class."""


import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        self.cli = None
        storage.reset()

    def test_help(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd("help")
            output = mock_stdout.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            self.assertTrue(storage.get("BaseModel", output))

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

            self.cli.onecmd("create BaseModel")
            obj_id = list(storage.all("BaseModel").keys())[0]

            self.cli.onecmd(f"show BaseModel {obj_id}")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd("destroy BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

            self.cli.onecmd("create BaseModel")
            obj_id = list(storage.all("BaseModel").keys())[0]

            self.cli.onecmd(f"destroy BaseModel {obj_id}")
            output = mock_stdout.getvalue().strip()
            self.assertFalse(storage.get("BaseModel", obj_id))
            self.assertIn("BaseModel", output)

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertFalse(output)

            self.cli.onecmd("create BaseModel")
            self.cli.onecmd("create BaseModel")
            self.cli.onecmd("create User")

            self.cli.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertIn("User", output)
            self.assertEqual(len(output.split('\n')), 3)

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd("update BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

            self.cli.onecmd("create BaseModel")
            obj_id = list(storage.all("BaseModel").keys())[0]

            self.cli.onecmd(f"update BaseModel {obj_id}")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

            self.cli.onecmd(f'update BaseModel {obj_id} name "John"')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
            self.assertNotIn("John", str(storage.get("BaseModel", obj_id)))

            self.cli.onecmd(f'update BaseModel {obj_id} name "John"')
            self.cli.onecmd(f'update BaseModel {obj_id} age 25')
            output = mock_stdout.getvalue().strip()
            self.assertIn("John", str(storage.get("BaseModel", obj_id)))
            self.assertIn("age", str(storage.get("BaseModel", obj_id)))


if __name__ == '__main__':
    unittest.main()
