def exists(a, x):
    l = 0
    r = len(a) - 1

    while l <= r:
        mid = (l + r) // 2

        if a[mid] == x:
            return True
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return False


a = [2, 4, 6, 8]
x = 5

print(exists(a, x))