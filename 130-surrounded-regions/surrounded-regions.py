class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        visited = [[False] * col for i in range(row)]
        def inmiddle(r, c):
            return 0 < r < row - 1 and 0 < c < col - 1
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col # the row and col are 0 indexed
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if not inbound(r,c) or board[r][c] == "X" or visited[r][c] == True:
                return
            visited[r][c] = True

            for dr, dc in direction:
                newr = dr + r
                newc = dc + c
                dfs(newr, newc)
        

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and not inmiddle(r,c):
                    dfs(r,c)
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and not visited[r][c]:
                    board[r][c] = "X"
        