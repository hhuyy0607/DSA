def bubble_sort_desc(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):

            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]

print("Mang ban dau:", arr)

bubble_sort_desc(arr)

print("Mang sau khi sap xep giam dan:", arr)