def factorial(num):
	if num == 0 or num == 1:
		return 1
	else:
		return num * factorial(num - 1)

sum2 = 0
sum1 = 0
for num in range(3,1000000):
	str1 = str(num)
	sum2 = 0
	for i in range(len(str1)):
		var = factorial(int(str1[i]))
		sum2 += var
	if sum2 == num:
		sum1 += num
print(sum1)
