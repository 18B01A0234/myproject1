def pythogeroan(i,j,k):
	if k * k == j * j + i * i:
		return 1
count = 0
for i in range(1,120):
	for j in range(1,120):
		for k in range(1,120):
			if i + j + k == 120:
				if pythogeroan(i,j,k):
					a,b,c = i,j,k
					count += 1
print(count-3)
