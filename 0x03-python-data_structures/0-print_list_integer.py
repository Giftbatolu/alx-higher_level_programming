#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ Print all the integer in the list.
        my_list:
            The list to print.
        Return: Nothing
    """
    for b in my_list:
        print("{:d}".format(b))
