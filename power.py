def power(num):
	num1 = num ** num
	return num1
sum = 0
for i in range(1,1000):
	sum += power(i)
num2 = str(sum)
print(num2[-10:])
