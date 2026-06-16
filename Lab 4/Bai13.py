a = [('An', 8), ('Ba', 5)]

n = len(a)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if a[j][1] < a[min_index][1]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print(a)