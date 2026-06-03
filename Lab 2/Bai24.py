def minimize_distance(stations, k):
    l = 0
    r = stations[-1] - stations[0]

    while r - l > 1e-6:
        mid = (l + r) / 2

        need = 0

        for i in range(1, len(stations)):
            gap = stations[i] - stations[i - 1]
            need += int(gap / mid)

        if need > k:
            l = mid
        else:
            r = mid

    return r


print(minimize_distance([1,2,3,4,5,6,7,8,9,10],9))