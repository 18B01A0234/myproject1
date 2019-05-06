def Next(n, li):
    count = 0
    for c in li:
        if c == n:
            if count == len(li)-1:
                return li[0]
            else:
                return li[count + 1]
        else:
            count += 1
                
def previous(n, li):
    count = 0
    for c in li:
        if c == n:
            return li[count - 1]
        else:
            count += 1

def previous_nth(n,x,li):
    for i in range(x):
        y = int(previous(n,li))
        n = y
    return y

def next_nth(n,x,li):
    for i in range(x):
        y = int(Next(n,li))
        n = y
    return y

def validity(n):
    count = 1
    y = str(n)
    for i in range(len(y)-1):
        if int(y[i]) >= int(y[i+1]):
            break
        else:
            count += 1
    if count == len(y):
        return n

def diff(n,li):
    return 
n = int(input())
x = int(input())
li = [x for x in range(10 ** (len(str(n))-1),10**(len(str(n)))) if validity(x)]
print('Previous Number:',previous(n,li))
print('Next number:',Next(n,li))
print(x,"previous Number",previous_nth(n,x,li))
print(x,"Next Number",next_nth(n,x,li))
print("Difference :",diff(n,li))
