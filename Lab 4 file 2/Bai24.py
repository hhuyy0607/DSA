def insertion_sort(a):
    a = a.copy()
    n = len(a)
    compare = 0
    shift = 0

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0:
            compare += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shift += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return compare, shift


def bubble_sort(a):
    a = a.copy()
    n = len(a)
    compare = 0
    swap = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            compare += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1

    return compare, swap


def selection_sort(a):
    a = a.copy()
    n = len(a)
    compare = 0
    swap = 0

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            compare += 1
            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1

    return compare, swap


a = [5, 2, 4, 6, 1, 3]

print("Insertion:", insertion_sort(a))
print("Bubble:", bubble_sort(a))
print("Selection:", selection_sort(a))