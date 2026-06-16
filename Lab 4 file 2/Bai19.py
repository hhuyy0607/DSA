a = [3, 2, 1]

i = 0
n = len(a)

while i < n:
    if i == 0 or a[i] >= a[i - 1]:
        i += 1
    else:
        a[i], a[i - 1] = a[i - 1], a[i]
        i -= 1

print(a)