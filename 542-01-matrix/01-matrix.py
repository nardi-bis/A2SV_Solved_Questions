class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        ans = [[-1] * col for r in range(row)]
        queue = deque()

        directions = [1, 0], [-1, 0], [0, -1], [0, 1]

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col


        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    ans[r][c] = 0
                    queue.append((r,c))
        while queue:
            x, y = queue.popleft()
            for dr, dc in directions:
                nr = dr + x
                nc = dc + y
                if inbound(nr, nc) and ans[nr][nc] == -1:
                    ans[nr][nc] =  ans[x][y] + 1
                    queue.append((nr,nc))
        return ans 
        
        
  
        