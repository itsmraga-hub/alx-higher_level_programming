#!/usr/bin/python3

import string

for i in string.ascii_lowercase:
	if not (i == 'q' or i == 'e'):
		print(i, end="")

