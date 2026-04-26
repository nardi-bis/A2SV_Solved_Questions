class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        # a binary search to find the row that the target is in
        top = 0
        bot = row - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if top > bot:
            return False

        mid = (top + bot) // 2
        l = 0
        r = col - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True
        return False


