#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for b in my_string:
        if b != 'c' and b != 'C':
            new_string += b
    return new_string
