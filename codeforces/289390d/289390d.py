n, m, k = map(int, input().split())
parent = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]

def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  root1 = find(x)
  root2 = find(y)

  if root1 == root2:
    return
  if size[root1] < size[root2]:
    root1, root2 = root2, root1

  parent[root2] = root1
  size[root1] += size[root2]

not_needed = []

for _ in range(m):
    not_needed.append(input())

ops = []

for i in range(k):
  command, u, v = input().split() 
  ops.append((command, int(u), int(v)))
ans = []  

for command, u, v in reversed(ops):
  if command == 'cut':
    union(u, v)
  else:
    ans.append("YES" if find(u) == find(v) else "NO")  

for a in reversed(ans):
  print(a)