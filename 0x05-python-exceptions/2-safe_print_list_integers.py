#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Function that print x elememts of a list.

    Arguments:
        my_list (a list): The list to print elements from.
        x (an integer): the number of elements to print.

    Returns:
        The number of elements printed.
    """
    num_elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_elements += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (num_elements)
