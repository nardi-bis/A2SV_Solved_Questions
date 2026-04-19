t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    currentr = 0
    max_r = 0
    for x in r:
        currentr += x
        if currentr > max_r:
            max_r = currentr
    
    currentb = 0
    max_b = 0
    for x in b:
        currentb += x
        if currentb > max_b:
            max_b = currentb
    
    print(max_r + max_b)