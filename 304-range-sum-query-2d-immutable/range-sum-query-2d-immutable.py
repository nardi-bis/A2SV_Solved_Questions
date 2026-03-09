class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.pre = [[0] * (m+2) for _ in range(n+2)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2+1][col2+1] - self.pre[row2+1][col1] - self.pre[row1][col2+1] + self.pre[row1][col1]