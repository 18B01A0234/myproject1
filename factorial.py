def factorial(num):
	if num == 0 or num == 1:
		return 1
	else:
		return num * factorial(num - 1)

num1 = factorial(10)
sum = 0
num2 = str(num1)
for i in range(len(num2)):
	sum += int(num2[i])
print(sum)
