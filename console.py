#!/usr/bin/python3
"""the entry point of the command interpreter:
"""


import cmd


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
        presses Ctrl+D"""
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

        args = line.split()
        class_name = args[0]
        if class_name not in storage.proj_classes():
            print("** class name missing **")
        

def do_create(self, line):
    """
    """
    args = line.split()
    if not args:
        print("Class name is missing")
        return

    class_name = args[0]

    if class_name not in class_mapping:
        print(f"Class '{class_name}' not found")
        return

    obj_class = class_mapping[class_name]
    new_object = obj_class()
    new_object.save()
    print(new_object.id)


def do_create(self, line):
        """Creates an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
