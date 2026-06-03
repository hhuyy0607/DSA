def can_put(pos, m, dist):
    count = 1
    last = pos[0]

    for i in range(1, len(pos)):
        if pos[i] - last >= dist:
            count += 1
            last = pos[i]

    return count >= m


def magnetic_force(pos, m):
    pos.sort()

    l = 1
    r = pos[-1] - pos[0]

    while l <= r:
        mid = (l + r) // 2

        if can_put(pos, m, mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans


print(magnetic_force([1,2,3,4,7],3))