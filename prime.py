def isprime(num):
	if num == 2 or num == 3:
		return True
	elif num % 2 ==0 and num % 3 == 0:
		return False
	r = 3
	while r * r <= num:
		if num % r == 0:
			return False
		r += 2
	return True
for i in range(2)
