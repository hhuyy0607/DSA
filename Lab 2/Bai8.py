def my_sqrt(n):
    l = 0
    r = n
    ans = 0

    while l <= r:
        mid = (l + r) // 2

        if mid * mid <= n:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans


print(my_sqrt(8))