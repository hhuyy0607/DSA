def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    l = 0
    r = m * n - 1

    while l <= r:
        mid = (l + r) // 2

        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False


matrix = [[1,3,5],[7,9,11]]
print(search_matrix(matrix, 9))