from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m1, m2 = map(int, input().split())
    
    f_edges = []
    for _ in range(m1):
        u, v = map(int, input().split())
        f_edges.append((u, v))

    # G
    pg = list(range(n + 1))
    def find_g(x):
        while pg[x] != x:
            pg[x] = pg[pg[x]]
            x = pg[x]
        return x
    def union_g(x, y):
        x, y = find_g(x), find_g(y)
        if x != y: pg[x] = y

    for _ in range(m2):
        a, b = map(int, input().split())
        union_g(a, b)

    # F
    pf = list(range(n + 1))
    def find_f(x):
        while pf[x] != x:
            pf[x] = pf[pf[x]]
            x = pf[x]
        return x
    def union_f(x, y):
        x, y = find_f(x), find_f(y)
        if x != y: pf[x] = y

    bad = 0
    for u, v in f_edges:
        if find_g(u) != find_g(v):
            bad += 1        # crosses G-components must remove
        else:
            union_f(u, v)   # valid edge

   
    gc_fc = defaultdict(set)
    for i in range(1, n + 1):
        gc_fc[find_g(i)].add(find_f(i))
    additions = sum(len(pieces) - 1 for pieces in gc_fc.values())

    print(bad + additions)