def first_pos(a, x):
    l, r = 0, len(a) - 1
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


def last_pos(a, x):
    l, r = 0, len(a) - 1
    ans = -1

    while l <= r:
        mid = (l + r) // 2

        if a[mid] == x:
            ans = mid
            l = mid + 1
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return ans


a = [1, 2, 2, 2, 3]
x = 2

f = first_pos(a, x)
l = last_pos(a, x)

if f == -1:
    print(0)
else:
    print(l - f + 1)