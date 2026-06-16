a = [5, 3, 1, 4, 2]
k = 2

n = len(a)

for i in range(k):
    min_index = i

    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print(a)