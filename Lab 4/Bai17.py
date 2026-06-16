a = [7, 2, 5, 1, 9]
k = 3

n = len(a)

for i in range(k):
    min_index = i

    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print("Phần tử nhỏ thứ", k, "là:", a[k - 1])