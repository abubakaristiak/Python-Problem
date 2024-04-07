a = list(map(lambda x: abs(int(x)), input().split(' ')))


if a[0] > a[1] and a[0] > a[2]:
    print(a[0], "eh o maior")
elif a[1] > a[2] and a[1] > a[0]:
    print(a[1], "eh o maior")
else:
    print(a[2], "eh o maior")
