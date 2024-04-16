#!/usr/bin/python3

""" Defines a finction that write to a file. """


def write_file(filename="", text=""):
    """
        function that write to a file.

        Args:
            filename - The file to write to.
            text - The text the write.

        Return: The written text.
    """

    with open(filename, "w", encoding="utf-8") as file_data:
        return(file_data.write(text))
