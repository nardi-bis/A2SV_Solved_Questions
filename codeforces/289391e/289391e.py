n, m = list(map(int, input().split()))
edges = []
for _ in range(m):
    b, e, w = map(int, input().split())
    edges.append((w, b, e))
edges.sort()
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False          # same component would form a cycle
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1
    return True
total_weight = 0
edges_used   = 0
for w, b, e in edges:
    if union(b, e):
        total_weight += w
        edges_used   += 1
        if edges_used == n - 1:   # MST complete
            break
print(total_weight)