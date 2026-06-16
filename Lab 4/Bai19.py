a = [5, 1, 4, 2, 8]

left = 0
right = len(a) - 1

while left < right:
    min_index = left
    max_index = left

    for i in range(left, right + 1):

        if a[i] < a[min_index]:
            min_index = i

        if a[i] > a[max_index]:
            max_index = i

    a[left], a[min_index] = a[min_index], a[left]

    if max_index == left:
        max_index = min_index

    a[right], a[max_index] = a[max_index], a[right]

    left += 1
    right -= 1

print(a)