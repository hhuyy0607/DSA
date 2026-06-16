a = [1, 2, 3]

n = len(a)
swap_count = 0

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    if min_index != i:
        a[i], a[min_index] = a[min_index], a[i]
        swap_count += 1

print("Mảng sau khi sắp xếp:", a)
print("Số lần hoán đổi:", swap_count)