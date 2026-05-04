t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    res = [nums[0]]

    for i in range(1, n - 1):
        if (nums[i - 1] < nums[i]) != (nums[i] < nums[i + 1]):
            res.append(nums[i])

    res.append(nums[n - 1])

    print(len(res))
    print(*res)