#!/usr/bin/python3
for num in range(10):
	for num2 in range(num + 1, 10):
		if num == 8 and num2 == 9:
			print(f"{num}{num2}")
		else:
			print(f"{num}{num2}", end = ", ")