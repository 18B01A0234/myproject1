sum1 = 0
for num in range(2,1000000):
	var = str(num)
	sum = 0
	for i in range(len(var)):
		var1 = int(var[i]) ** 5
		sum += var1
	if sum == num:
		sum1 += num
print(sum1)
