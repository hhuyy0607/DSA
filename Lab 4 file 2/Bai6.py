a = [1, 2, 3]

n = len(a)
compare_count = 0

for i in range(1, n):
    key = a[i]
    j = i - 1

    while j >= 0:
        compare_count += 1

        if a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        else:
            break

    a[j + 1] = key

print("Mảng sau khi sắp xếp:", a)
print("Số lần so sánh:", compare_count)