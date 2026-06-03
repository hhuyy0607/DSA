def find_closest(a, k, x):
    l = 0
    r = len(a) - k

    while l < r:
        mid = (l + r) // 2

        if x - a[mid] > a[mid + k] - x:
            l = mid + 1
        else:
            r = mid

    return a[l:l+k]


print(find_closest([1,2,3,4,5],4,3))