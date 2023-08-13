#!/usr/bin/python3
"""
The module contains HBNBCommand class
"""
import cmd
import models
import ast
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter
    """
    prompt = '(hbnb) '
    __classes = ["BaseModel", "Amenity", "City", "Place",
                 "Review", "State", "User"]

    def command_args(self, line):
        """
        Check if the command arguments follow a certain instructions.
        """
        line = self.clean_line(line)
        args = []
        if line:
            args = line.split()
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return []
        else:
            print("** class name missing **")
        return args

    def clean_line(self, line):
        "Clean a line from trailing spaces (whitespace, tabs, newline)"
        clean_line = line
        if clean_line:
            clean_line = line.split()
            clean_line = ' '.join(clean_line)
        return clean_line

    def emptyline(self):
        """this function does nothing when pressing
        empty line"""
        pass

    def do_EOF(self, line):
        'Exit the program'
        print("")
        return True

    def do_quit(self, line):
        'Exit the program.'
        return True

    def do_create(self, line):
        "Creates a new instance of given class."
        args = self.command_args(line)
        if args:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name.
        """
        args = self.command_args(line)
        if args:
            if len(args) <= 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objs = models.storage.all()
                if key in objs.keys():
                    print(objs[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        'Deletes an instance based on the class name and id.'
        args = self.command_args(line)
        if args:
            if len(args) <= 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objs = models.storage.all()
                if key in objs.keys():
                    del objs[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of
        all instances based or not on the class name.
        """
        objs = models.storage.all()
        inst_list = []
        if line:
            args = self.command_args(line)
            if args:
                cls_exists = any(key.startswith(args[0]) for key in objs)
                if cls_exists:
                    inst_list = [str(value) for key, value in objs.items()
                                 if key.startswith(args[0])]
            else:
                return
        else:
            inst_list = [str(objs[key]) for key in objs]
        print(inst_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        args = self.command_args(line)
        objs = models.storage.all()
        if args:
            if len(args) <= 1:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) not in objs.keys():
                print("** no instance found **")
            elif len(args) <= 2:
                print("** attribute name missing **")
            elif len(args) <= 3:
                print("** value missing **")
            elif args[2] not in ["id", "created_at", "updated_at"]:
                value = args[3]
                try:
                    value = ast.literal_eval(args[3])
                except ValueError:
                    pass
                if type(value) in [str, int, float]:
                    instance = objs["{}.{}".format(args[0], args[1])]
                    instance.__dict__[args[2]] = value
                    instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
