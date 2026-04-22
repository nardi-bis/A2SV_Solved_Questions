class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        island = 0

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        visited = [[False] * col for i in range(row)]

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r,c):
            if not inbound(r, c) or grid[r][c] == "0" or visited[r][c]:
                return
            visited[r][c] = True
            
            for r_change, c_change in directions:
                new_r = r + r_change
                new_c = c + c_change
                # visited[new_r][new_c] = True
                dfs(new_r, new_c)
 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    island += 1
        return island












        