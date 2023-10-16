#!/usr/bin/python3
"""the entry point of the command interpreter:
"""


import cmd
import json
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand
    """
    prompt = "(hbnb) "

    def do_quit(self, argum):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, argum):
        """Thi exits the command interpreter when user
        presses Ctrl+D
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when line is empty and ENTER is pressed"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if line is None or line == "":
            print("Class name is missing")
        else:
            args = line.split()
            class_name = args[0]
            if class_name not in storage.proj_classes():
                print("** class doesn't exist **")
            else:
                new_instance = storage.proj_classes()[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        if class_name not in storage.proj_classes():
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        if class_name not in storage.proj_classes():
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Prints the string representation of instances."""
        args = line.split()

        if args:
            class_name = args[0]
            if class_name not in storage.proj_classes():
                print("** class doesn't exist **")
                return
            insts = [str(obj) for key, obj in storage.all().items()
                     if isinstance(obj, storage.proj_classes()[class_name])]
        else:
            insts = [str(obj) for key, obj in storage.all().items()]

        print(insts)

    def do_update(self, line):
        """Updates an instance by adding or
        updating an attribute.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.proj_classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, value)
        instance.save()

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
