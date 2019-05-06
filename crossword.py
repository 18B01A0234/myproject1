a = ''
count = 1
rows = int(input("read no.of rowss"))
columns = int(input("readno.of columns"))
li = []
list1 = []
li1 = []
for i in range(rows):
    x = input() 
    li.append(x)
print("Across:")
for i in li:
    i = i.split('*')
    while '' in i:
        i.remove('')
	for j in i:
            print(j)
print('Down:')
for i in range(columns):
    b = ''
    for j in range(rows):
        if li[j][i] == '*':
            break
        else:
            b += li[j][i] 
            li1.append(b)
for i in range(1,rows):
