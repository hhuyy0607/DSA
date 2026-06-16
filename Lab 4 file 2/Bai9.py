a = [5, 2, 4, 6, 1, 3]

compare_count = 0
shift_count = 0


def binary_search(a, key, left, right):
    global compare_count

    while left <= right:
        mid = (left + right) // 2
        compare_count += 1

        if a[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return left


n = len(a)

for i in range(1, n):
    key = a[i]

    pos = binary_search(a, key, 0, i - 1)

    j = i - 1

    while j >= pos:
        a[j + 1] = a[j]
        shift_count += 1
        j -= 1

    a[pos] = key

print("Mảng sau khi sắp xếp:", a)
print("Số lần so sánh:", compare_count)
print("Số lần dịch chuyển:", shift_count)