class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0
      

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 1 :
                    ans += 4
                if inbound(r-1,c) and grid[r-1][c] == 1:
                    ans -= 1
                if inbound(r+1,c) and grid[r+1][c] == 1:
                    ans -= 1
                if inbound(r,c-1) and grid[r][c-1] == 1:
                    ans -= 1
                if inbound(r,c+1) and grid[r][c+1] == 1:
                    ans -= 1
                print(r, c, ans)
                # if grid[r-1][c] and grid[r-1][c] == 1:
                #     ans -= 1
                # if grid[r+1][c] and grid[r+1][c] == 1:
                #     ans -= 1
                # if grid[r][c-1] and grid[r][c-1]== 1:
                #     ans -= 1
                # if grid[r][c+1] and grid[r][c+1] == 1:
                #     ans -= 1
                
        return ans
        