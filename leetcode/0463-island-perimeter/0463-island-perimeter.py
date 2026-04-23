class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def inbound(r, c):
            return 0 <= r < row and 0 <= c <col

        visited = [[False] * col for i in range(row)]

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if not inbound(r, c):
                return 1
            if grid[r][c] == 0:
                return 1
            if visited[r][c]:
                return 0
            
            visited[r][c] = True # next if we come back again we will return 0 
            perimeter = 0

            for r_change, c_change in directions:
                new_row = r + r_change
                new_col = c + c_change

                perimeter += dfs(new_row, new_col)            
            print(perimeter)   
            return perimeter
            
        # to find the first land
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r, c) 
        return 0



        