def isprime(num):
	if num == 2 or num == 3:
		return True
	if num % 2 == 0 or num % 3 == 0:
		return False
	for num1 in range(4,num // 2):
		if num % num1 == 0:
			return False
	return True
def isfactor(num):
	factor = 2
	factors = []
	while num > 2:
		if num % factor == 0:
			if isprime(factor):
				factors.append(factor)
				num //= factor
		factor += 1
	return factors
max1 = max(isfactor(600851475143))
print(max1)
		
