#!/usr/bin/python3
def print_last_digit(num):
	if num >= 0:
		last = num % 10
	else:
		last = -1 * (num % -10)

	print("{:d}".format(last), end='')
	return last
