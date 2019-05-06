first = 1
second = 1
third = 0
count = 3
while third < 10 ** 1100:
	third = first + second
	first = second
	second = third
	var = str(third)
	if len(var) == 1000:
		x = third
		break
	count += 1
print(count)
