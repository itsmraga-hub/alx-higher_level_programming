#!/usr/bin/python3
def print_last_digit(num):
    if num >= 0:
        last = num % 10
    else:
        last = num % -10
        last *= -1
    print("{:d}".format(last), end='')
    return (last)
