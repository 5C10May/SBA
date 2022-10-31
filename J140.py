n = int(input())

for i in range(1, n+1):
    a = i*i
    print(a, end=' ')
    for j in range (n-1):
        a = a+i
        print(a, end=' ')
    print(end='\n')
