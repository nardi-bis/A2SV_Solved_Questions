class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS
        graph = defaultdict(list)
        indegree = [0] * numCourses
        queue = [] # to traverse
        res = []
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            x = queue.pop(0)
            res.append(x)

            # for v in graph.values():
            for v in graph[x]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        if len(res) != numCourses:
            return []
        else:
            return res

                





     
        
            




