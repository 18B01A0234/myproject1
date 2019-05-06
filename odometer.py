def validity(read2):
	if int(read2[-1])== 0 or int(read2[0]) == 0 or int(read2[1]) <= int(read2[0]) or int(read2) > 99:
	        return 0
	return 1

reading = int(input())
read = str(reading)
read1 = read
if int(read[-1])== 0 or int(read[0]) == 0 or int(read[1]) <= int(read[0]) or reading > 99:
	print("Invalid")
else:
	if validity(str(reading-1)):
		print('previous reading:',reading - 1)
	else:
		x = (int(read[0]) - 1) * 10 + 9
		if x <= 9:
			print("Previous Reading : 89")
		else:
			print("Previous Reading:",x)
	if validity(str(reading+1)):
		print('Next Reading:',reading+1)
	else:
		y = (int(read[0])+1) * 10 +(int(read[0])+2)
		if y >= 90:
			print("Next Number : 12")
		else:
			print('Next Reading:',y)
