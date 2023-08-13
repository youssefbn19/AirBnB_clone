#!/usr/bin/python3
"""
The module contains HBNBCommand class
"""
import cmd
import models
import ast
import re
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

    def default(self, line):
        """
        Checks special commands
        """
        reg = r'^(\w+)\.(\w+)\((.*)\)'
        check_line = re.match(reg, line)
        if check_line:
            args = check_line.groups()
            if args[1] == "all":
                self.all(args[0])
            elif args[1] == "count":
                self.count(args[0])
            elif args[1] == "show":
                key = "{} {}".format(args[0], args[2].replace("\"", ""))
                self.do_show(key)
                # self.show(args[0], args[2])
        else:
            super().default(line)

    def command_args(self, line):
        """
        Check if the command arguments follow a certain instructions.
        """
        line = self.clean_line(line)
        args = []
        if line:
            args = line.split()
            print("coolab {}".format(args))
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
        """handle new lines"""
        pass

    def do_EOF(self, line):
        'Exit the program'
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

    def check_class(self, cls):
        """
        Checks if the given class is exist in the list of classes
        """
        if cls in HBNBCommand.__classes:
            return True
        else:
            print("** class doesn't exist **")
            return False

    def list_instances(self, objs, cls):
        """
        Return a dictionary of instances of a specific class
        """
        instances = {key: value for key, value in objs.items()
                     if key.startswith(cls)}
        return instances

    def all(self, cls_name):
        """
        Retrieve all instances of a given class
        """
        objects = models.storage.all()
        if self.check_class(cls_name):
            instances = self.list_instances(objects, cls_name)
            result = [str(value) for value in instances.values()]
            concat = ", ".join(result)
            print("[{}]".format(concat))

    def count(self, cls_name):
        """
        Retrieve the number of instances of a class
        """
        objects = models.storage.all()
        if self.check_class(cls_name):
            instances = self.list_instances(objects, cls_name)
            print(len(instances))

    # def show(self, cls_name, id=""):
    #    """
    #    Retrieve an instance based on its ID
    #    """
    #    objects = models.storage.all()
    #    if self.check_class(cls_name):
    #        if id:
    #            instances = self.list_instances(objects, cls_name)
    #            arg = "{}.{}".format(cls_name, id.replace("\"", ""))
    #            print(arg)
    #            if any(key == arg for key in instances):
    #                print(instances[arg])
    #            else:
    #                print("** no instance found **")
    #        else:
    #            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
