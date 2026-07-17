class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])

        visited = [[False] * col for r in range(row)]

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        directions = [1, 0], [-1, 0], [0, -1], [0, 1]
        ans = copy.deepcopy(image)

        def dfs(r, c):
            if not inbound(r, c) or visited[r][c] or image[r][c] != image[sr][sc]:
                return
            ans[r][c] = color
            visited[r][c] = True
            for r_change, c_change in directions:
                dfs(r_change + r, c_change + c)
       

        dfs(sr, sc)
        return ans