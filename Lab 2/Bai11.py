def find_min(a):
    l = 0
    r = len(a) - 1

    while l < r:
        mid = (l + r) // 2

        if a[mid] > a[r]:
            l = mid + 1
        else:
            r = mid

    return a[l]


a = [3, 4, 5, 1, 2]
print(find_min(a))