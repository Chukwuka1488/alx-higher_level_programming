#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    value = abs(number) % 10
    value = -1 * value
else:
    value = number % 10

if value > 5:
    print(f"Last digit of {number} is {value} and is greater than 5")
elif value == 0:
    print(f"Last digit of {number} is 0 and is {value}")
else:
    print(f"Last digit of {number} is {value} and is less than 6 and not 0")
