#!/usr/bin/python3
"""Module for the HBNB Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """This method implements quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when input is an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

