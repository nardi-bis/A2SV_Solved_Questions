class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row = col = len(grid)
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col
        visited = [[False] * col for _ in range(row)]
        queue = deque()

        def dfs(r, c):
            if not inbound(r,c) or visited[r][c] or grid[r][c] == 0:
                return
            visited[r][c] = True
            queue.append((r, c))

            for nr, nc in directions:
                new_r = nr + r
                new_c = nc + c
                dfs(new_r, new_c)

        found = False
        # only the first island call dfs 
        for r in range(row):
            if found:
                break
            for c in range(col):
                if grid[r][c] == 1:
                    found = True
                    dfs(r, c)
                    break
        flip = 0
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for new_r, new_c in directions:
                    nr = new_r + x
                    nc = new_c + y
                    if not inbound(nr,nc) or visited[nr][nc]:
                        continue
                    if grid[nr][nc] == 0:
                        queue.append((nr,nc))
                        visited[nr][nc] = True
                    if grid[nr][nc] == 1:
                        return flip

            flip += 1
        return -1
                



        