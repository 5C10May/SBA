import math
a, b, c =(input()).split()
a = int(a)
b = int(b)
c = int(c)
d = b*b - 4*a*c
if d > 0:
    e = (-b + math.sqrt(d)) / (2*a)
    f = (-b - math.sqrt(d)) / (2*a)
    if e < f:
        print(format(e, ".3f"), end=' ')
        print(format(f, ".3f"))
    else:
        print(format(f, ".3f"), end=' ')
        print(format(e, ".3f"))
elif d == 0:
    e = (-b + math.sqrt(d)) / (2*a)
    print(format(e, ".3f"))
else:
    print("None")
