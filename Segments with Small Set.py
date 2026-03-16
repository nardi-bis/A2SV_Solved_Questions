from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = defaultdict(int)
left = 0
unique = 0
result = 0

for r in range(n):
    if count[a[r]] == 0:
        unique += 1
    count[a[r]] += 1

    while unique > k:
        count[a[left]] -= 1
        if count[a[left]] == 0:
            unique -= 1
        left += 1
    result += (r - left + 1)
print(result)
