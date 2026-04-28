class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        row = len(height)
        col = len(height[0])
        pac = set()
        atl = set()

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col
        directions = [[1, 0],[0, 1],[-1, 0],[0, -1]]

        def dfs(r, c, visited):
            visited.add((r, c)) # why not check if it is inbound 

            for a, b in directions:
                new_r = r + a
                new_c = c + b
                if inbound(new_r, new_c) and (new_r, new_c) not in visited and height[r][c] <= height[new_r] [new_c]:
                    dfs(new_r, new_c, visited)
        
        for i in range(row): # the left and the right
            dfs(i, 0, pac) 
            dfs(i, col - 1, atl) 
        for i in range(col): # to the top and the down
            dfs(0, i, pac)
            dfs(row - 1, i, atl)

        res = []
        for i in range(row):
            for j in range(col):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res



        