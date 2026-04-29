class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        white = 1
        gray = 2
        black = 3
        color = {k: white for k in range(numCourses)} # we use dictionary and make all the value white
        adj_list = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            adj_list[pre].append(course)

        no_cycle = True
        stack = []

        def dfs(node):
            nonlocal no_cycle

            if not no_cycle:
                return 
            color[node] = gray
            for n in adj_list[node]:
                if color[n] == white:
                    dfs(n)
                elif color[n] == gray:
                    no_cycle = False
                    return
            color[node] = black
            stack.append(node)
        

        for c in range(numCourses):
            if color[c] == white:
                dfs(c)

        if not no_cycle:
            return []
        return stack[::-1]




          
            
        