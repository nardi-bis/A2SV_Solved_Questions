h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())
horizontal = [[0] * (w + 1) for _ in range(h + 1)]
vertical = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        horizontal[i][j] = horizontal[i - 1][j] + horizontal[i][j - 1] - horizontal[i - 1][j - 1]
        vertical[i][j] = vertical[i - 1][j] + vertical[i][j - 1] - vertical[i - 1][j - 1]

        if j < w and grid[i - 1][j - 1] == '.' and grid[i - 1][j] == '.':
            horizontal[i][j] += 1

        if i < h and grid[i - 1][j - 1] == '.' and grid[i][j - 1] == '.':
            vertical[i][j] += 1
q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    x = horizontal[r2][c2 - 1] - horizontal[r1 - 1][c2 - 1] - horizontal[r2][c1 - 1] + horizontal[r1 - 1][c1 - 1]
    y = vertical[r2 - 1][c2] - vertical[r1 - 1][c2] - vertical[r2 - 1][c1 - 1] + vertical[r1 - 1][c1 - 1]

    print(x + y)