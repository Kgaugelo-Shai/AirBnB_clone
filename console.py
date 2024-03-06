#!/usr/bin/python3
""" Defines the command line interpreter to manage AirBnB objects. """
import cmd
# Imports cmd class
# Entry point
# My main function is defined here
# create class that inherits from cmd class
# Define __init__ class that inherits the parent class __init__ method
# and define an empty dictionary
# set prompt to "(hbnb) "
class ClientManager(cmd.Cmd):
    """ Defines a ClientManager class that inherits from the cmd class """
    prompt = "(hbnb) "
    def __init__(self):
        """ Initializes a ClientManager class object """
        super().__init__()
        self.client = {} # dictionary to store clients.

    def do_EOF(self, line):
        print()
        return True

    def help_EOF(self):
        print("Terminates the command line interpreter safely using ctrl + d ")

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Terminates the command line safely using the keyword quit ")

    def default(self, line):
        print(f"Unknown command: {line}")


if __name__ == "__main__":
    """
    Creates a ClientManager object and parses the object to a cmdloop method
    """
    ClientManager().cmdloop()