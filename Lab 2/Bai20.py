def allocate_books(pages, m):
    l = max(pages)
    r = sum(pages)

    while l < r:
        mid = (l + r) // 2

        students = 1
        cur = 0

        for p in pages:
            if cur + p > mid:
                students += 1
                cur = 0

            cur += p

        if students <= m:
            r = mid
        else:
            l = mid + 1

    return l


print(allocate_books([12,34,67,90],2))