a = [1, 2, 4, 3, 5, 6, 8, 7]

n = len(a)

shift_count = 0

for i in range(1, n):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        shift_count += 1
        j -= 1

    a[j + 1] = key

print("Mảng sau khi sắp xếp:", a)
print("Số shift:", shift_count)