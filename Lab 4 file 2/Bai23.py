def insertion_sort(a):
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


best = [1, 2, 3, 4, 5]
avg = [3, 1, 5, 2, 4]
worst = [5, 4, 3, 2, 1]

print("Best case:", insertion_sort(best.copy()))
print("Average case:", insertion_sort(avg.copy()))
print("Worst case:", insertion_sort(worst.copy()))