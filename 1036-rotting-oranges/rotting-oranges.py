class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque()

        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        fresh = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        minute = 0
        while queue:
            rotted_this_round = False
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dr, dc in directions:
                    nr = dr + x
                    nc = dc + y
                    if inbound(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
                        rotted_this_round = True
            if rotted_this_round:
                minute += 1
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
        return minute
        #     if rotted_this_round:
        #         minute += 1
        # return minute if fresh == 0 else -1

            
        #     minute += 1
    

        




        