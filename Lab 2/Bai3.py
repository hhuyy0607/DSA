def first_occurrence(a, x):
    l = 0
    r = len(a) - 1
    ans = -1

    while l <= r:
        mid = (l + r) // 2

        if a[mid] == x:
            ans = mid
            r = mid - 1
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return ans


a = [1, 2, 2, 2, 3]
print(first_occurrence(a, 2))