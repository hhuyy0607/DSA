import math

def binary_search(arr, key):

    mid = 0

    left = 0

    right = len(arr) - 1

    step = 0

    while (left <= right):

        step = step + 1

        mid = (left + right) // 2

        print("Lan lap thu:", step)
        print("left =", left, "right =", right, "mid =", mid)
        print("Gia tri tai mid =", arr[mid])
        print("-------------------")

        if (key == arr[mid]):
            return mid

        if (key < arr[mid]):
            right = mid - 1

        else:
            left = mid + 1

    return -1


arr = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]

key = 40

result = binary_search(arr, key)

print("Vi tri tim kiem thu i la:", result)


print("\nNhan xet:")
print("Input: Mang da sap xep va gia tri can tim")
print("Output: Vi tri cua phan tu trong mang")
print("Neu khong tim thay se tra ve -1")