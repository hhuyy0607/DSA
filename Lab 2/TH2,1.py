def binary_search(array, x):

    left = 0
    right = len(array) - 1

    while left <= right:

        mid = (left + right) // 2

        if array[mid] == x:
            return mid

        elif x < array[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1


array = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]

x = 28

result = binary_search(array, x)

if result != -1:
    print("Phan tu tim thay tai vi tri:", result)
else:
    print("Khong tim thay phan tu")