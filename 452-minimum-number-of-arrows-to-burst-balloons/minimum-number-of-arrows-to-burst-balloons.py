class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow=1
        points.sort()
        current_end=points[0][1]
        for i in range(1,len(points)):
            start,end=points[i]
            if current_end>=start:
                current_end=min(end,current_end)
            else:
                arrow+=1
                current_end=end
        return arrow