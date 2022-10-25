y1, m1, d1 =(input()).split()
y2, m2, d2 =(input()).split()
y1 = int(y1)
m1 = int(m1)
d1 = int(d1)
y2 = int(y2)
m2 = int(m2)
d2 = int(d2)
if y1 < y2:
    print("Before")
elif y1 > y2:
    print("After")
else:
    if m1 < m2:
        print("Before")
    elif m1 > m2:
        print("After")
    else:
        if d1 < d2:
            print("Before")
        elif d1 > d2:
            print("After")
        else:
            print("Same")
