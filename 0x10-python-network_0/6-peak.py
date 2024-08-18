#!/usr/bin/python3

def find_peak(list_of_integers):
    """
        A function that find the peak value of a list of integer.

        Args (int):
            list_of_integers - The list to find the peak value of.

        Return:
            If the is not none return the peak value.
            If the list is none return None
    """

    if list_of_integers == []:
        return None

    list_of_integers.sort()
    return list_of_integers[-1]
