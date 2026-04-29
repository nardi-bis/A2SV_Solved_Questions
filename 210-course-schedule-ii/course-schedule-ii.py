class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        white = 1
        gray = 2
        black = 3
        color = {k: white for k in range(numCourses)} # we use dictionary and make all the value white
        res = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            res[pre].append(course)

        no_cycle = True
        stack = []

        def dfs(node):
            nonlocal no_cycle

            if not no_cycle:
                return 
            color[node] = gray
            for n in res[node]:
                if color[n] == white:
                    dfs(n)
                elif color[n] == gray:
                    no_cycle = False
                    return
            color[node] = black
            stack.append(node)
            return True

        for c in range(numCourses):
            if color[c] == white:
                dfs(c)

        if not no_cycle:
            return []
        return stack[::-1]




          
            
        