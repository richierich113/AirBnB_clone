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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
