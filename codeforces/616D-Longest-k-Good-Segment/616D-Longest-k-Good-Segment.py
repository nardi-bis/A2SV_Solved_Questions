from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = Counter()
left = 0
res = 0
idx = []

for right in range(n):
    freq[a[right]] += 1

    while len(freq) > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            del freq[a[left]]
        left += 1
    
    if right - left + 1 > res:
        res = right - left + 1
        idx = [left + 1, right + 1]
print(*idx)