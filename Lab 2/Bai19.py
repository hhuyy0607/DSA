def can_place(stalls, cows, dist):
    count = 1
    last = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            count += 1
            last = stalls[i]

    return count >= cows


def aggressive_cows(stalls, cows):
    stalls.sort()

    l = 1
    r = stalls[-1] - stalls[0]

    while l <= r:
        mid = (l + r) // 2

        if can_place(stalls, cows, mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans


print(aggressive_cows([1,2,4,8,9],3))