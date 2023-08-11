#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1
args_list = argv[1:]

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
    print("1: {}".format(args_list[0]))
else:
    print("{} arguments:".format(num_args))
    for i, arg in enumerate(args_list, start=1):
        print("{}: {}".format(i, arg))
