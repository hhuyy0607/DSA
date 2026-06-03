def binary_search(a, x):
    l = 0
    r = len(a) - 1

    while l <= r:
        mid = (l + r) // 2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1


a = [1, 3, 5, 7, 9]
x = 7

print(binary_search(a, x))