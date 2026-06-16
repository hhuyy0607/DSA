a = [5, 2, 4, 6, 1, 3]

n = len(a)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print("Mảng sau khi sắp xếp:", a)