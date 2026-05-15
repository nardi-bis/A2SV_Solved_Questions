from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    
    prev = float('-inf')
    possible = True
    
    for x in a:
        options = []
        
        if x >= prev:
            options.append(x)
        
        i = bisect_left(b, prev + x)
        if i < m:
            options.append(b[i] - x)
        if not options:
            possible = False
            break
        prev = min(options)
    
    print("YES" if possible else "NO")