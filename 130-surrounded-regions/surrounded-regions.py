class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        visited = [[False] * col for r in range(row)]
        directions = [[1, 0],[0, 1],[-1, 0],[0, -1]]
        

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col
            
        def change(r,c):
            return 0 < r < row - 1 and 0 < c < col - 1
        
        def dfs(r, c):
            if not inbound(r, c) or board[r][c] == "X" or visited[r][c]:
                return
            visited[r][c] = True
            

            for r_change, c_change in directions:
                new_r = r + r_change
                new_c = c + c_change
                dfs(new_r, new_c)

                
                

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and not change(r, c):
                    dfs(r, c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and not visited[r][c] :
                    board[r][c] = "X"
