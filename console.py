#!/usr/bin/python3
""" Defines the command line interpreter to manage AirBnB objects. """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
# Imports cmd class
# Entry point
# My main function is defined here
# create class that inherits from cmd class
# Define __init__ class that inherits the parent class __init__ method
# and define an empty dictionary
# set prompt to "(hbnb) "
class HBNBCommand(cmd.Cmd):
    """ Defines a ClientManager class that inherits from the cmd class """
    prompt = "(hbnb) "

    __instances = {
            "BaseModel": BaseModel
        }
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
        print("Quit command to exit the program")

    def default(self, line):
        if len(line) ==  0:
            return
        print(f"Unknown command: {line}")

    def emptyline(self):
        """does nothing upon recieving an empty command."""
        pass

    def do_create(self, line):
        """ creates a new instance of BaseModel, saves it ad prints id. """
        #create - creates a new instance of BaseModel
        # savesit (to JSON File) and prints id
        # Ex: create BaseModel
        # if the class name is missing, print ** class name missing **(ex: $ create)
        # If the class name doesn’t exist, print ** class doesn't exist **
        # (ex: $ create MyModel)
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__instances:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.__instances[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """ Prints the string representation of an instance based on the
            class name Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__instances:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            fileStorage = FileStorage()
            fileStorage.reload()
            instance = fileStorage.all().get(f"{args[0]}.{args[1]}")
            if instance:
                print(instance)
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the
           class name. Ex: $ all BaseModel or $ all
        """
        # reload our file, save it to a dict object
        # iterate through the dictionary object
        # print every value of the required class

        fileStorage = FileStorage()
        # reload everything in our JSON file
        fileStorage.reload()
        # return dict representation of all our instances
        dict_instance = fileStorage.all()
        if not line:
            print([str(v) for k,v in dict_instance.items()])
        elif line:
            #loop through the keys dict_instance
            # if key == line, print value
            print([str(v) for k,v in dict_instance.items()
                           if line == k.split(".")[0]])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """ Deletes an instance based on class name and id,
            save the change to JSON file.
            Ex: $ destroy BaseModel 1234-1234-1234
        """
        fileStorage = FileStorage()
        fileStorage.reload()
        obj_dict = fileStorage.all()
        args = line.split()

        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__instances:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(args[0],args[1])

            if k not in obj_dict:
                print("**no instance found**")
            else:
                del obj_dict[k]
                fileStorage.save()
    
    def do_update(self,line):
        """Updates an instance based on the class name and id
           by adding or updating attribute save the JSON file.
           Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        fileStorage = FileStorage()
        fileStorage.reload()
        instance = fileStorage.all()
        args = line.split()

        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__instances:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        



if __name__ == "__main__":
    """
    Creates a ClientManager object and parses the object to a cmdloop method
    """
    HBNBCommand().cmdloop()
