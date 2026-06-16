a = [5, 2, 4, 6, 1]

n = len(a)

for i in range(n - 1):
    max_index = i

    for j in range(i + 1, n):
        if a[j] > a[max_index]:
            max_index = j

    a[i], a[max_index] = a[max_index], a[i]

print("Mảng sau khi sắp xếp:", a)