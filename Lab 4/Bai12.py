a = [(2, 'a'), (2, 'b'), (1, 'c')]

n = len(a)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if a[j][0] < a[min_index][0]:
            min_index = j

    key = a[min_index]

    while min_index > i:
        a[min_index] = a[min_index - 1]
        min_index -= 1

    a[i] = key

print(a)