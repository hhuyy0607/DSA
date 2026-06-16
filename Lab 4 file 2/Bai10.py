a = [2, 4, 1, 3]

n = len(a)

shift_count = 0
inversion_count = 0


b = a.copy()

for i in range(1, n):
    key = b[i]
    j = i - 1

    while j >= 0 and b[j] > key:
        b[j + 1] = b[j]
        shift_count += 1
        j -= 1

    b[j + 1] = key


for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            inversion_count += 1

print("Số lần dịch chuyển:", shift_count)
print("Số nghịch thế:", inversion_count)