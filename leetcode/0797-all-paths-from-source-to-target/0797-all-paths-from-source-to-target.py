class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        destination = n-1

        def dfs(node,path):
            if path and path[-1] == destination:
                ans.append(path[:])
                return


            for neighbour in graph[node]:
                path.append(neighbour)

                dfs(neighbour,path)

                path.pop()
        dfs(0,[0])

        return ans