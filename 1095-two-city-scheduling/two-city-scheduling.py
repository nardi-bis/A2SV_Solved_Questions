class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        res = 0
        for ca,cb in costs:
            diff.append([cb - ca, ca, cb])
        diff.sort()
        for i in range(len(diff)):
            if len(diff) // 2 > i:
                res += diff[i][2]
            else:
                res += diff[i][1]
        return res



        