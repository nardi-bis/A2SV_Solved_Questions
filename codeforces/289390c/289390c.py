def find(x):
    global parent, offset
    if x == parent[x]:
        return x
    par = parent[x]
    parent[x] = find(parent[x])
    offset[x] += offset[par]
    return parent[x]
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return
    if size[rootX] < size[rootY]:
        rootX, rootY = rootY, rootX
    size[rootX] += size[rootY]
    parent[rootY] = rootX
    offset[rootY] = base[rootY] - base[rootX]
def add(x, v):
    rootX = find(x)
    base[rootX] += v
def get(x):
    rootX = find(x)
    return base[rootX] + offset[x]
n, m = map(int, input().split())
parent = list(range(n))
size = [1] * n
offset = [0] * n
base = [0] * n
for _ in range(m):
    cmd, *nums = input().split()
    nums = list(map(int, nums))
    if cmd == 'add':
        add(nums[0] - 1, nums[1])
    elif cmd == 'join':
        union(nums[0] - 1, nums[1] - 1)
    else:
        print(get(nums[0] - 1))