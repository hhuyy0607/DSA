import heapq

a = [7, 2, 5, 1, 9, 3]
k = 3


b = a.copy()

n = len(b)

for i in range(k):
    min_index = i

    for j in range(i + 1, n):
        if b[j] < b[min_index]:
            min_index = j

    b[i], b[min_index] = b[min_index], b[i]

print("Partial Selection:", b[:k])


c = a.copy()

heapq.heapify(c)

result = []

for i in range(k):
    result.append(heapq.heappop(c))

print("Heap:", result)