a = [(2, 'a'), (2, 'b'), (1, 'c')]

n = len(a)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if a[j][0] < a[min_index][0]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print(a)