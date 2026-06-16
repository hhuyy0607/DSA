a = []
data = [5, 2, 8, 1]

for x in data:
    a.append(x)

    i = len(a) - 2

    while i >= 0 and a[i] > x:
        a[i + 1] = a[i]
        i -= 1

    a[i + 1] = x

    print(a)