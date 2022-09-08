n = int(input())
m = n-1
x = 1
for i in range(n+1):
    for j in range(i):
        print(x, end='') #don't start a new line
        x = x+1
    print() #new line
    
while m > 0:
    for j in range(m):
        print(x, end='')
        x = x+1
    print()
    m = m-1
