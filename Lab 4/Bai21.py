a = [5, 2, 4, 1, 3]

n = len(a)
compare_count = 0

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        compare_count += 1

        if a[j] < a[min_index]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print("Mảng sau khi sắp xếp:", a)
print("Số lần so sánh:", compare_count)
print("Công thức:", n * (n - 1) // 2)