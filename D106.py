n = input()
m = n[-1:]

if n[-2:] == "1":
    print(n + "th")
elif m == '1':
    print(n + "st")
elif m == '2':
    print(n + "nd")
elif m == '3':
    print(n + "rd")
else:
    print(n + "th")
