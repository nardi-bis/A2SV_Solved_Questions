class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list) # bomb -> list of bomb that it can detonate
        for i in range(len(bombs)):
            for j in range(1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2)**2 + (y1 - y2)**2)

                if d <= r1:
                    adj[i].append(j)
                if d <= r2:
                    adj[j].append(i)

        def dfs(i,visited):
            if i in visited:
                return 0
            visited.add(i)
            for neibour in adj[i]:
                dfs(neibour, visited)
            return len(visited)

        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res
