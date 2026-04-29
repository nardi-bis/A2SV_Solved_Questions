n = int(input())
tree = [[] for _ in range(n)]
for i in range(1, n):
    parent = int(input())
    tree[parent - 1].append(i)  
for node in range(n):
    if len(tree[node]) > 0:
        leaf_count = 0
        for child in tree[node]:
            if len(tree[child]) == 0:
                leaf_count += 1
        if leaf_count < 3:
            print("No")
            exit()

print("Yes")