def isprime(num):
	if num == 2 or num == 3:
		return True
	for num1 in range(4,num // 2):
		if num % num1 == 0:
			return False
	return True	 
sum1 = 0
for i in range(2,2000000):
	if isprime(i):
		sum1 += i

print(sum1)
