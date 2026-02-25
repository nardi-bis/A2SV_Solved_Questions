class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        diri, dirj = 0, 1 
        twice = 2
        res = []
        moves = 1
        next_moves = 2
        while len(res) < (rows * cols):
            if (-1 < rStart < rows) and ( -1 < cStart < cols):
                res.append([rStart,cStart])
            rStart += diri
            cStart += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri 
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return res
