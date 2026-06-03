def ship(weights, D):
    l = max(weights)
    r = sum(weights)

    while l < r:
        mid = (l + r) // 2

        days = 1
        cur = 0

        for w in weights:
            if cur + w > mid:
                days += 1
                cur = 0

            cur += w

        if days <= D:
            r = mid
        else:
            l = mid + 1

    return l


print(ship([1,2,3,4,5,6,7,8,9,10],5))