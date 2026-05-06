class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = [[] for i in range(n + 1)]

        for pre, course in relations:
            graph[course].append(pre)
        
        complete_times = [0 for i in range(n + 1)]

        def dfs(course):
            nonlocal complete_times

            if complete_times[course]:
                return complete_times[course]
            
            max_prereq = 0
            
            for pre in graph[course]:
                max_prereq = max(max_prereq, dfs(pre))
            
            complete_times[course] = max_prereq + time[course - 1]
            
            return complete_times[course]
        
        for i in range(1, n + 1):
            if not complete_times[i]:
                dfs(i)
        
        return max(complete_times)
        
        

        