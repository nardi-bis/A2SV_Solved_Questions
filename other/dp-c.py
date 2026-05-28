import sys
sys.setrecursionlimit(10**6)
n = int(input())
days = []
for _ in range(n):
    a, b, c = map(int, input().split())
    days.append((a, b, c))
memo = {}
def dp(i, last):
    if i == n:
        return 0
    if (i, last) not in memo:
        best = 0
        for act in range(3):
            if act != last:
                best = max(best, days[i][act] + dp(i + 1, act))
        memo[(i, last)] = best
    return memo[(i, last)]

print(dp(0, -1))