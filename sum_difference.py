sum1 = 0
sum2 = 0
for num in range(1,101):
	sum1 = sum1 + num ** 2
	sum2 = sum2 + num
diff = (sum2 ** 2) - sum1
print(diff)
