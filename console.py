#!/usr/bin/python3
"""Module for the HBNB Console"""
import cmd
from models.base_model import BaseModel

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

    def do_create(self, arg):
        """Create a new instance, saves it, and prints the id"""
        from models import storage
        if not arg:
            print("** class name missing **")
            return
        try:
            # Check if the class is in my_classes
            class_name = arg
            my_classes = storage.get_my_classes()
            if class_name not in my_classes:
                print("** class doesn't exist **")
                return
            # Create an instance using the class from my_classes
            new_instance = my_classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        from models import storage
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            my_classes = storage.get_my_classes()

            if class_name not in my_classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()

            if key in instances:
                obj_instance = my_classes[class_name](**instances[key])
                print(obj_instance)
            else:
                print("** no instance found **")

        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        from models import storage
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            my_classes = storage.get_my_classes()

            if class_name not in my_classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()

            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        from models import storage
        args = arg.split()
        instances_list = []

        try:
            # Get the dictionary of supported classes
            my_classes = storage.get_my_classes()

            if not args:
                # If no class name provided, show all instances
                for value in storage.all().values():
                    instances_list.append(str(value))
            else:
                class_name = args[0]
                # Check if the provided class name is valid
                if class_name not in my_classes:
                    print("** class doesn't exist **")
                    return

                # Iterate through instances and filter by class name
                for key, value in storage.all().items():
                    if class_name == key.split('.')[0]:
                        instances_list.append(str(value))

            #print the list of instances
            print(instances_list)
        except NameError:
            print("** class doesn't exists **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        from models import storage
        args = arg.split()
        keys = [x.split('.')[0] for x in storage.all().keys()]

        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            my_classes = storage.get_my_classes()

            if class_name not in my_classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()

            if key in instances:
                if len(args) < 3:
                    print("** attribute name missing **")
                    return

                attribute_name = args[2]

                if len(args) < 4:
                    print("** value missing **")
                    return

                attribute_value = args[3]
                obj_instance = my_classes[class_name](**instances[key])
                setattr(obj_instance, attribute_name, attribute_value)
                obj_instance.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
