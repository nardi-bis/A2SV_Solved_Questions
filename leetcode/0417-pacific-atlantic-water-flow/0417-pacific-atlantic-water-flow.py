class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1,0), (1,0), (0, 1), (0, -1)]
        n = len(heights)
        m = len(heights[0])
        pac = set()
        atl = set()

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col, visited):
            visited.add((row, col))

            for a,b in directions:
                nrow = row + a
                ncol = col + b

                if inbound(nrow, ncol):
                    if (nrow, ncol) not in visited and heights[row][col] <= heights[nrow][ncol]:
                        dfs(nrow, ncol, visited)

        for i in range(m): 
            dfs(0, i, pac)
            dfs(n-1, i, atl)
        for i in range(n):
            dfs(i, 0, pac)
            dfs(i, m-1, atl)

        res = []
        for i in range(n):
            for j in range(m):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res