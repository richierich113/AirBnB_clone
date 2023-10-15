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
	    else:
            args = line.split()
            class_name = args[0]
            if class_name not in storage.proj_classes():
                print("** class doesn't exist **")
            else:
                new_intance = storage.classes()[class_name]()
                new_intance.save()
                print(new_intance.id)

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
