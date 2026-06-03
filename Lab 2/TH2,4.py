def binary_search(arr, x):

    left = 0
    right = len(arr) - 1
    step = 0

    while left <= right:

        step = step + 1

        mid = (left + right) // 2

        print("Lan lap thu:", step)
        print("left =", left)
        print("right =", right)
        print("mid =", mid)
        print("Gia tri tai mid =", arr[mid])
        print("-------------------")

        # neu tim thay
        if arr[mid] == x:
            return mid

        # neu x nho hon mid
        elif x < arr[mid]:
            right = mid - 1

        # nguoc lai tim ben phai
        else:
            left = mid + 1

    # khong tim thay
    return -1


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print("Mang ban dau:")
print(arr)

# cau a
x = 95

print("\nTim kiem x =", x)

result = binary_search(arr, x)

if result != -1:
    print("Tim thay tai vi tri:", result)
else:
    print("Khong tim thay phan tu trong mang")


# cau b
x = 5

print("\nTim kiem x =", x)

result = binary_search(arr, x)

if result != -1:
    print("Tim thay tai vi tri:", result)
else:
    print("Khong tim thay phan tu trong mang")