#!/usr/bin/python3

def read_file(filename=""):
    """ Function that read fron a text file and print to stdout.

    Arg:
        filename - The file to read.
    """
    with open(filename, 'r', encoding="utf-8") as file_data:
        for line in file_data:
            print(line, end="")
