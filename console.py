#!/usr/bin/python3
import cmd
from models import base_model
BaseModel = base_model.BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def default(self, line):
        """nothing to print"""
        pass

    def emptyline(self):
        """empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        quit()

    def do_EOF(self, line):
        """End Of File"""
        quit()

    def do_create(self, line):
        """
        """
        print(my_obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()