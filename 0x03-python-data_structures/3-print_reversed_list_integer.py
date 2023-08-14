#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        print None
    while n >= 0:
        print("{:d}".format(my_list[n]))

