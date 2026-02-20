class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows=1
        current_end = points[0][1]
        
        for i in range(1, len(points)):
            start, end = points[i]
            
            if start <= current_end:
                current_end = min(current_end, end)
            else:
                arrows += 1
                current_end = end
        
        return arrows

