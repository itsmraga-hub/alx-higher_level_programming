def uppercase(str):
	for i in range(len(str)):
		if ord(str[i]) >= 97 and ord(str[i]) <= 122:
			n = 32
		else:
			n = 0
		print("{:c}".format(ord(str[i]) - n), end='')
	print()
