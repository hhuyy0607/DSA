def upper_bound(a, x):
    l = 0
    r = len(a)

    while l < r:
        mid = (l + r) // 2

        if a[mid] <= x:
            l = mid + 1
        else:
            r = mid

    return l


a = [1, 3, 5, 7]
print(upper_bound(a, 5))