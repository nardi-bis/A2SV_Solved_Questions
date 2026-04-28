class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        
        self.sumMat = [[0] * (col + 1) for i in range(row + 1)]

        for i in range(row):
            prefix = 0
            for j in range(col):
                prefix += matrix[i][j]
                above = self.sumMat[i][j + 1]# was supposed to be self.sumMat[i - 1][j] but there is and additional row and col added with the value of 0
                self.sumMat[i + 1][j + 1] = prefix + above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomright = self.sumMat[r2][c2]
        # the above row that is going to be subtracted
        above = self.sumMat[r1 - 1][c2]
        #the left col that is going to be subtracted
        left = self.sumMat[r2][c1 - 1] 
        topleft = self.sumMat[r1 - 1][c1 - 1] 
        return bottomright - above - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)