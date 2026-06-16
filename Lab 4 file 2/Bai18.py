a1 = [1, 2, 3, 4, 5]
x = 6

compare_right = 0

i = len(a1) - 1

while i >= 0:
    compare_right += 1

    if a1[i] > x:
        i -= 1
    else:
        break

print("Dò từ phải sang trái:", compare_right, "lần so sánh")


a2 = [1, 2, 3, 4, 5]

compare_left = 0

i = 0

while i < len(a2):
    compare_left += 1

    if a2[i] < x:
        i += 1
    else:
        break

print("Dò từ trái sang phải:", compare_left, "lần so sánh")