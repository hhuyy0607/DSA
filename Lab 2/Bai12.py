def find_peak(a):
    l = 0
    r = len(a) - 1

    while l < r:
        mid = (l + r) // 2

        if a[mid] < a[mid + 1]:
            l = mid + 1
        else:
            r = mid

    return l


a = [1, 2, 3, 1]
print(find_peak(a))