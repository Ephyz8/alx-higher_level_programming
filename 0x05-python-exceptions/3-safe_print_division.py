#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        dvd = a / b
    except (TypeError, ZeroDivisionError):
        dvd = None
    finally:
        print("Inside result: {}".format(dvd))
    return (dvd)
