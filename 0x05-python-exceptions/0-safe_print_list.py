#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    #printed_num = 0
    try:
        printed_num = 0
        for b in range(x):
            print(my_list[b], end="")

            printed_num += 1
    except IndexError:
        pass
    print()
    return printed_num
