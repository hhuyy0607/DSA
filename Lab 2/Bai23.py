def kth_smallest(matrix, k):
    n = len(matrix)

    l = matrix[0][0]
    r = matrix[n-1][n-1]

    while l < r:
        mid = (l + r) // 2

        count = 0
        col = n - 1

        for row in range(n):
            while col >= 0 and matrix[row][col] > mid:
                col -= 1

            count += col + 1

        if count < k:
            l = mid + 1
        else:
            r = mid

    return l


matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]

k = 8

print(kth_smallest(matrix, k))