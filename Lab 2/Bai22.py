def find_median(a, b):
    if len(a) > len(b):
        a, b = b, a

    m = len(a)
    n = len(b)

    l = 0
    r = m

    while l <= r:
        i = (l + r) // 2
        j = (m + n + 1) // 2 - i

        leftA = float('-inf') if i == 0 else a[i-1]
        rightA = float('inf') if i == m else a[i]

        leftB = float('-inf') if j == 0 else b[j-1]
        rightB = float('inf') if j == n else b[j]

        if leftA <= rightB and leftB <= rightA:

            if (m+n) % 2 == 0:
                return (max(leftA,leftB)+min(rightA,rightB))/2
            else:
                return max(leftA,leftB)

        elif leftA > rightB:
            r = i - 1
        else:
            l = i + 1


print(find_median([1,3],[2]))