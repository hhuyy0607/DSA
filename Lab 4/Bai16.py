a = [-3, 1, -2, 2]

n = len(a)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if abs(a[j]) < abs(a[min_index]):
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print(a)