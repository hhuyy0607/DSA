def search_rotated(a, target):
    l = 0
    r = len(a) - 1

    while l <= r:
        mid = (l + r) // 2

        if a[mid] == target:
            return mid

        if a[l] <= a[mid]:
            if a[l] <= target < a[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if a[mid] < target <= a[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


a = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(a, 0))