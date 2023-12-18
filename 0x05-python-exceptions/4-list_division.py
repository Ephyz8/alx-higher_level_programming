#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    n_lst = []
    for i in range(0, list_length):
        try:
            dvd = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            dvd = 0
        except ZeroDivisionError:
            print("division by 0")
            dvd = 0
        except IndexError:
            print("out of range")
            dvd = 0
        finally:
            n_lst.append(dvd)
    return (n_lst)
