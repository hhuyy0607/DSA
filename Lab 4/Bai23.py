def selection_sort(a):
    n = len(a)

    compare_count = 0
    swap_count = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            compare_count += 1

            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swap_count += 1

    return a, compare_count, swap_count


a1 = [1, 2, 3, 4, 5]
a2 = [3, 1, 5, 2, 4]
a3 = [5, 4, 3, 2, 1]

print("Best case:")
print(selection_sort(a1))

print("Average case:")
print(selection_sort(a2))

print("Worst case:")
print(selection_sort(a3))