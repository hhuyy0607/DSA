import heapq

a1 = [5, 2, 4, 1, 3]
a2 = [5, 2, 4, 1, 3]

n = len(a1)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if a1[j] < a1[min_index]:
            min_index = j

    a1[i], a1[min_index] = a1[min_index], a1[i]

print("Selection Sort:", a1)


heapq.heapify(a2)

result = []

while a2:
    result.append(heapq.heappop(a2))

print("Heap Sort:", result)