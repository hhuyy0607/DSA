def min_eating_speed(piles, h):
    l = 1
    r = max(piles)

    while l < r:
        mid = (l + r) // 2

        hours = 0
        for p in piles:
            hours += (p + mid - 1) // mid

        if hours <= h:
            r = mid
        else:
            l = mid + 1

    return l


print(min_eating_speed([3,6,7,11],8))