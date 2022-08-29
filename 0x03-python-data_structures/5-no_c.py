#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]

    j = 0
    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new_string = new_string[:(i - j)] + my_string[(i + 1):]
            j += 1

    return new_string
