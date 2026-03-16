t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    white = s[:k].count('W')
    min_ = white

    for right in range(k, n):
        if s[right - k] == 'W':
            white -= 1
        if s[right] == 'W':
            white += 1
        min_ = min(min_, white)
    print(min_)