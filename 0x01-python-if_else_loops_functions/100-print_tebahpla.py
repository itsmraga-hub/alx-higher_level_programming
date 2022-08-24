#!/usr/bin/python3
for c in reversed(range(97, 123)):
    print("{:c}".format(c if (c % 2 == 0) else (c - 32)), end='')
