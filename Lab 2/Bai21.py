def split_array(nums, k):
    l = max(nums)
    r = sum(nums)

    while l < r:
        mid = (l + r) // 2

        groups = 1
        cur = 0

        for x in nums:
            if cur + x > mid:
                groups += 1
                cur = 0

            cur += x

        if groups <= k:
            r = mid
        else:
            l = mid + 1

    return l


print(split_array([7,2,5,10,8],2))