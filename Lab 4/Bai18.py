a1 = [5, 4, 3, 2, 1]
a2 = [5, 4, 3, 2, 1]

n = len(a1)

selection_swap = 0

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if a1[j] < a1[min_index]:
            min_index = j

    if min_index != i:
        a1[i], a1[min_index] = a1[min_index], a1[i]
        selection_swap += 1


bubble_swap = 0

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a2[j] > a2[j + 1]:
            a2[j], a2[j + 1] = a2[j + 1], a2[j]
            bubble_swap += 1

print("Selection Sort:", a1)
print("Số swap Selection:", selection_swap)

print("Bubble Sort:", a2)
print("Số swap Bubble:", bubble_swap)