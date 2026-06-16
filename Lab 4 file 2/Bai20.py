a = [8, 5, 3, 7, 6, 2, 1, 4]

n = len(a)
gap = n // 2

while gap > 0:

    for i in range(gap, n):
        temp = a[i]
        j = i

        while j >= gap and a[j - gap] > temp:
            a[j] = a[j - gap]
            j -= gap

        a[j] = temp

    print("Gap =", gap, ":", a)

    gap //= 2