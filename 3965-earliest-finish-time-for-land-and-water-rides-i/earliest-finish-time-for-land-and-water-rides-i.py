class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for i in range(len(landStartTime)):
            landEnd = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                finish = max(landEnd, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, finish)

        for j in range(len(waterStartTime)):
            waterEnd = waterStartTime[j] + waterDuration[j]
            for i in range(len(landStartTime)):
                finish = max(waterEnd, landStartTime[i]) + landDuration[i]
                ans = min(ans, finish)
        return ans