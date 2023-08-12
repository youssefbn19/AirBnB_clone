#!/usr/bin/python3
"""
The module contains HBNBCommand class
"""
import cmd
from models.base_model import BaseModel
import models
import ast


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter
    """
    prompt = '(hbnb) '
    __classes = ["BaseModel"]

    def command_args(self, line):
        """
        Check if the command arguments follow a certain instructions.
        """
        if line:
            if line not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                return True
        else:
            print("** class name missing **")
        return False

    def clean_line(self, line):
        "Clean a line from trailing spaces (whitespace, tabs, newline)"
        clean_line = line
        if clean_line:
            clean_line = line.split()
            clean_line = ' '.join(clean_line)
        return clean_line

    def do_EOF(self, line):
        'Exit the program'
        return True

    def do_quit(self, line):
        'Exit the program.'
        return True

    def do_create(self, line):
        "Creates a new instance of given class."
        line = self.clean_line(line)
        print(line)
        inst = self.command_args(line)
        if inst:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name.
        """
        line = self.clean_line(line)
        args = line.split()
        check_args = self.command_args(args[0])
        if check_args:
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
        line = self.clean_line(line)
        args = line.split()
        check_args = self.command_args(args[0])
        if check_args:
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
        line = self.clean_line(line)
        objs = models.storage.all()
        if line:
            cls_exists = any(key.startswith(line) for key in objs)
            if cls_exists:
                inst_list = [str(value) for key, value in objs.items()
                             if key.startswith(line)]
            else:
                print("** class doesn't exist **")
                return
        else:
            inst_list = [str(objs[key]) for key in objs]
        print(inst_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        line = self.clean_line(line)
        args = line.split()
        check_args = self.command_args(args[0])
        objs = models.storage.all()
        if check_args:
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
