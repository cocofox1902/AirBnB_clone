#!/usr/bin/python3
"""
the Commande translator
"""
import cmd
import re
from models.base_model import BaseModel
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex


class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """
    All the instance used listed:
        default(self, arg):
        emptyline(self):
        do_quit(self, arg):
        do_EOF(self, arg):
        do_create(self, arg):
        do_show(self, arg):
        do_destroy(self, arg):
        do_count(self, cls_name):
    public instance atributs: prompt(str): the commande start
    """
    prompt = '(hbnb) '

    def default(self, arg):
        list_of_arg = arg.split('.')
        fisrt = "all()"
        second = "count()"
        third = "show"
        fourth = "destroy"
        aux = list_of_arg[1]
        aux = aux.split("\"")
        name = list_of_arg[1].split('(')
        try:
            if list_of_arg[1] == fisrt:
                self.do_all(list_of_arg[0])
        except Exception:
            pass
        try:
            if list_of_arg[1] == second:
                self.do_count(list_of_arg[0])
        except Exception:
            pass
        try:
            if name[0] == third:
                arguments = list_of_arg[0] + " " + aux[1]
                self.do_show(arguments)
        except Exception:
            pass
        try:
            if name[0] == fourth:
                arguments = name[0] + " " + aux[1]
                self.do_destroy(arguments)
        except Exception:
            pass

    def emptyline(self):
        """empty arg
        """
        pass

    def parse(arg):
        """Convert a series of zero or more numbers to an argument tuple"""
        return shlex.split(arg)

    def do_quit(self, arg):
        """Quit command to exit the program
        USE: $ quit
        """
        return True

    def do_EOF(self, arg):
        """End Of File to quit the file
        USE: $ EOF
        """
        print()
        return True

    def do_create(self, arg):
        """create to create a new instance
        USE: $ create
        """
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            print(new.id)
            new.save()

    def do_show(self, arg):
        """show to print the string representation
        of an instance based on the class name and id
        USE: $ show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return False
        data = shlex.split(arg)
        if data[0] not in class_dict.keys():
            print("** class doesn't exist **")
            return False
        if len(data) == 1:
            print("** instance id missing **")
            return False
        classNameId = f"{data[0]}.{data[1]}"
        print(classNameId)
        print(models.storage.all())
        if classNameId not in models.storage.all():
            print("** no instance found **")
            return False
        print(models.storage.all()[classNameId])

    def do_destroy(self, arg):
        """destroy to Deletes an instance based on the class name and id
        USE: destoy <class name> <id>
        """
        name = arg.split()
        kw = ".".join(name)
        if not name:
            print("** class name missing **")
        elif name[0] not in globals():
            print("** class doesn't exist **")
        elif len(name) == 1:
            print("** instance id missing **")
        elif kw not in models.storage.all():
            print("** no instance found **")
        else:
            dic = models.storage.all()
            if kw in dic:
                del dic[kw]
                models.storage.save()

    def do_all(self, arg):
        """all to Prints all string representation
        of all instances based or not on the class name
        USE: all <class name> or all
        """
        if not arg or arg in globals():
            for value in models.storage.all().values():
                print([str(value)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update to Updates an instance based
        on the class name and id by adding or updating attribute
        USE: update <class name> <id> <attribute name> "<attribute value>
        """
        args = arg.split()
        kw = ".".join(args[:2])
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif ".".join(args[:2]) not in models.storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            kw = ".".join(args[:2])
            atributs = args[2]
            value = args[3]
            _dict = models.storage.all()[kw].__dict__
            _dict[atributs] = value
            models.storage.save()

    def do_count(self, cls_name):
        """count to retrieve the number of instances of a class
        USE: User.count()
        """
        try:
            count = 0
            for k, _ in (models.storage.all()).items():
                if cls_name in k:
                    count += 1
            print(count)
        except Exception:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
