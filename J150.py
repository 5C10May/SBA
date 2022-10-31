n = int(input())

a = 1
for i in range(n):
    print(a, end=' ')
    for j in range (n-1):
        a = a+4
        print(a, end=' ')
    print(end='\n')
