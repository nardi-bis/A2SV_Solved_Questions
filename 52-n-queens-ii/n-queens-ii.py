class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = [-1] * n 

        def is_valid(row, col):
            for r in range(row):
                if cols[r] == col or abs(cols[r] - col) == abs(r - row):
                    return False
            return True

        def solve(row):
            nonlocal count
            if row == n:
                count += 1
                return            
            for col in range(n):
                if is_valid(row, col):
                    cols[row] = col
                    solve(row + 1)
        solve(0)
        return count