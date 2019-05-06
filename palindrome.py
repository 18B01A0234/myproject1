def revs(num):
	num1 = str(num)
	if num1[::-1] == num1:
		return True
	return False
list1 = []
for num in range(999,99,-1):
	for num1 in range(100,1000):
		product = num * num1
		if revs(product):
			list1.append(product)
max1 = max(list1)
print(max1)
