n, k, q = map(int,input().split())
maxtemp = 200000
pre = [0] * (maxtemp + 2)
for _ in range(n):
    l, r = map(int,input().split())
    pre[l] += 1
    pre[r+1] -= 1
for i in range(1, maxtemp+1):
    pre[i] +=pre[i-1]
for i in range(1, maxtemp+1):
    if pre[i] >= k:
        pre[i] = 1
    else:
        pre[i] = 0
for i in range(1, maxtemp+1):
    pre[i] +=pre[i-1]
# answer 
for _ in range(q):
    a, b = map(int,input().split())
    print(pre[b] - pre[a-1])
