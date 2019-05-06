first = 1
second = 2
third = first + second
sum1 = second
while third < 4000000:
	first = second
	second = third
	third = first + second
	if third % 2 == 0:
		sum1 += third
print(sum1)
