num1 = 2 ** 15
num2 = str(num1)
sum = 0
for i in range(len(num2)):
	sum += int(num2[i])
print(sum)
