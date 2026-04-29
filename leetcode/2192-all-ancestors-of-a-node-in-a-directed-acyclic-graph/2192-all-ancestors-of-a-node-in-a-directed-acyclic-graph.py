class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for i in range(n)]
        res = []
        for v, k in edges:
            adj[k].append(v)

        def dfs(node, ancestor):
            for parent in adj[node]: # parent of node
                if parent not in ancestor:
                    ancestor.add(parent)
                    dfs(parent,ancestor)

        for i in range(n):
            anc = set()
            dfs(i,anc)
            res.append(list(sorted(anc)))
        return res

        
        # def dfs(node):
        #     if not node and look[node] == []:
        #         return
        #     n -= 1
        
        #     for n in look[node]:
        #         dfs(n)

        #         adj[node].append(look[n])

        # dfs(n - 1)
        # return adj


        
    