class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def back(start, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            for i in range(start,n+1):
                path.append(i)
                back(i+1,path)
                path.pop()
        back(1, [])
        return ans
        